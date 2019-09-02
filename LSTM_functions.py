
import numpy as np
from sklearn.model_selection import StratifiedKFold

from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform

#definition of default hyperparameters dictionary
# which governs all training settings

def get_default_hyperparameters():
    return {\
    "negative_positive_ratio":1,\
    "n_epochs":50, \
    "n_folds":5,\
    "batch_size":32\
    }


#compute word embeddings from a piece of text
#keep the grouping of words into sentences

#arguments:  mapping   = pandas dataframe
#                          this defines mapping from words to vectors
#                          columns are vectors: column names are words, rows are vector dimensions
#            sentences = list of sentences
#                          each sentence is a string
#            output    = output type, can be "index_list", "index_matrix" or "full_embedding_list" (see description of return value)

#return:    sentence_embeddings = list or matrix of embedded sentences
#             if output == "index_list":
#             return list of embedded sentences, each embedded sentence is a vector of indices into embedding matrix
#             if output == "index_matrix":
#             return matrix of embedded sentences,
#             if output == "full_embedding_list"
#             return list of embedded sentences, each embedded sentence is a M x N matrix
#             where M is embedding space dimension, N is number of tokens in the sentence
#
def embed_sentences(mapping, sentences, output="index"):

    sentence_embeddings = []
    for s in sentences:
        single_word_embeddings = []
        words = s.split()
        for w in words:
            if(w in mapping.columns):
                if(output=="full_embedding_list"):
                    single_word_embeddings.append(mapping[w].values[:,np.newaxis])
                elif(output in ["index_list", "index_matrix"]):
                    single_word_embeddings.append(mapping.columns.get_loc(w))
        if(len(single_word_embeddings) > 1):
            if(output=="full_embedding_list"):
                sentence_embeddings.append(np.concatenate(single_word_embeddings, axis=1))
            elif(output in ["index_list", "index_matrix"]):
                sentence_embeddings.append(np.array(single_word_embeddings))
    if(output in ["full_embedding_list", "index_list"]):
        return sentence_embeddings
    else:
        max_len = np.max(np.array([len(e) for e in sentence_embeddings]))
        embedding_matrix = np.zeros([len(sentence_embeddings), max_len])
        for k,e in enumerate(sentence_embeddings):
            embedding_matrix[k,0:len(e)] = e
        return embedding_matrix


# embedding layer converts indices to full index_vectors
# this is the first stage of the LSTM model
def pretrained_embedding_layer(embedding_df):

    embedding_layer = Embedding(embedding_df.shape[1] + 1, embedding_df.shape[0], trainable=False)
    embedding_layer.build((None,))
    embed_matrix = np.transpose(embedding_df.values)
    embed_matrix = np.concatenate([embed_matrix, np.zeros([1, embed_matrix.shape[1]])], axis=0)
    embedding_layer.set_weights([embed_matrix])
    return embedding_layer

# return graph describing LSTM model
def LSTM_graph(max_len, embedding_df):
    index_vectors = Input(shape=(max_len,) , dtype='int32')
    embedding_layer = pretrained_embedding_layer(embedding_df)
    embeddings = embedding_layer(index_vectors)
    X = LSTM(units=128, return_sequences=True)(embeddings)
    X = Dropout(rate=0.5)(X)
    # Propagate X trough another LSTM layer with 128-dimensional hidden state
    # Here the returned output is a single hidden state, not a batch of sequences.
    X = LSTM(units=128, return_sequences=False)(X)
    # Add dropout with a probability of 0.5
    X = Dropout(rate=0.5)(X)
    # Single sigmoid output unit
    X = Dense(units=1, activation='sigmoid')(X)

    # Create Model instance which converts sentence_indices into X.
    model = Model(inputs=index_vectors, outputs=X)

    return model

# train LSTM model
# hp = hyperparameters
# hp["n_folds"] > 1 : do crossvalidation, return out-of-fold prediction for each point
# hp["n_folds"] < 1 : no crossvalidation
def train_LSTM(positives, negatives, mapping, hp=get_default_hyperparameters(), ):

    full_embedded              = embed_sentences(mapping, positives + negatives, "index_matrix")
    positive_embedded = full_embedded[0:len(positives),:]
    negative_embedded = full_embedded[len(positives):,:]

    n_positive = len(positives)
    if(hp["negative_positive_ratio"] > 0):
        n_negative = int(np.floor(hp["negative_positive_ratio"]*n_positive))
        assert n_negative <= negative_embedded.shape[0], "insufficient negative data for this negative/positive ratio"
    else:
        n_negative = len(negatives)
    negative_indices = np.random.permutation(negative_embedded.shape[0])[0:n_negative]
    negative_embedded_sub = negative_embedded[negative_indices,:]


    training_mat = np.concatenate([positive_embedded, negative_embedded_sub], axis=0)
    labels = np.array([1]*n_positive + [0]*n_negative)
    training_cases  = positives + [negatives[i] for i in negative_indices]
    #these are the cases that are actually used for training
    #return them in case they are useful for error analysis

    if(hp["n_folds"]>1):
        #first step:
        #use crossvalidation to estimate performance on hold-out data
        #the model versions trained here are not returned! they are discarded
        skf = StratifiedKFold(n_splits = hp["n_folds"], random_state = 33, shuffle=True)
        out_of_fold_preds = np.nan*np.ones([training_mat.shape[0], 1])
        #predictions made when the given data point was in holdout set

        for k, (train_indices, test_indices) in enumerate(skf.split(training_mat, labels)):
            print('\nTraining LSTM on fold %d / %d :\n'%(k+1, hp["n_folds"]))
            model = LSTM_graph(training_mat.shape[1], mapping)
            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            model.fit(training_mat[train_indices,:], labels[train_indices],\
                      epochs=hp["n_epochs"], batch_size=hp["batch_size"], shuffle=True)
            out_of_fold_preds[test_indices,:] = model.predict(training_mat[test_indices,:])
    #now do not use crossvalidation
    #just train on all data provided
    #to obtain the final trained model, which is returned
    model = LSTM_graph(training_mat.shape[1], mapping)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(training_mat, labels, epochs=hp["n_epochs"], batch_size=hp["batch_size"], shuffle=True)

    return (model, out_of_fold_preds, labels, training_cases)

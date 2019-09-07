# MIT License
#
# Copyright (c) 2019 Colin James Stoneking

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#-------------------------------------------------------------------------------


import numpy as np
import pandas as pd
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
    "n_negative":1000,\
    "n_positive":1000,\
    "n_neutral":1000,\
    "n_epochs":50, \
    "n_folds":5,\
    "batch_size":32,\
    "max_words_per_sentence":50\
    }

#convert a python 3 unicode string to printable ASCII
#which is defined as space, punctuation, letters, digits
#this function is used on all strings that are passed to the model
#for training or prediction
def string_to_printable_ascii(s):
    return "".join([c for c in s if ord(c) >= 32 and ord(c) <= 126])

#load GloVe data
#this can take a bit of time, especially for the higher-dimensional datasets (such as 300d)
#so report progress
def load_glove(path):
    with open(path) as f:
        n_entries = 0
        d = 0

        for k, line in enumerate(f.readlines()):
            n_entries = k + 1
            #the first entry is "the", it is well formatted
            if(k==0): d = len(line.split()) - 1
        glove_data = np.zeros([d, n_entries])
        words = []
        #store each entry (word) as column
        print('Found %d words in glove dataset'%n_entries)
        f.seek(0)
        for k, line in enumerate(f.readlines()):
            lst = line.split()
            words.append(lst[0])
            vals = np.array([float(s) for s in lst[1:]])
            glove_data[:,k] = vals
            if(k % 50000==0):
                print('Words loaded : %06d '%k)
        print('Finished loading data')

    return( pd.DataFrame(glove_data, columns=words))

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
def embed_sentences(mapping, sentences, output="index", max_len=0):

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
        if(max_len==0):
            max_len = np.max(np.array([len(e) for e in sentence_embeddings]))
        embedding_matrix = np.zeros([len(sentence_embeddings), max_len])
        for k,e in enumerate(sentence_embeddings):
            if(len(e)<= max_len):
                embedding_matrix[k,0:len(e)] = e
            else:
                embedding_matrix[k,:] = e[0:max_len]
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

    #X = Dense(units=1, activation='sigmoid')(X) # Single sigmoid output unit
    X = Dense(units=3, activation='softmax')(X)

    # Create Model instance which converts sentence_indices into X.
    model = Model(inputs=index_vectors, outputs=X)

    return model

# train LSTM model
# hp = hyperparameters
# hp["n_folds"] > 1 : do crossvalidation, return out-of-fold prediction for each point
# hp["n_folds"] < 1 : no crossvalidation
def train_LSTM(positives, negatives, neutrals, mapping, hp=get_default_hyperparameters() ):

    positives = [string_to_printable_ascii(s) for s in positives]
    negatives = [string_to_printable_ascii(s) for s in negatives]
    neutrals  = [string_to_printable_ascii(s) for s in neutrals]

    max_len = hp["max_words_per_sentence"]

    full_embedded     = embed_sentences(mapping, positives + negatives + neutrals, "index_matrix", max_len)
    positive_embedded = full_embedded[0:len(positives),:]
    negative_embedded = full_embedded[len(positives):(len(positives) + len(negatives)),:]
    neutral_embedded  = full_embedded[(len(positives) + len(negatives)):,:]

    n_positive = hp["n_positive"]
    n_negative = hp["n_negative"]
    n_neutral  = hp["n_neutral"]

    assert n_positive <= positive_embedded.shape[0], "insufficient positive data provided"
    assert n_negative <= negative_embedded.shape[0], "insufficient negative data provided"
    assert n_neutral  <= neutral_embedded.shape[0], "insufficient neutral data provided"

    positive_indices = np.random.permutation(positive_embedded.shape[0])[0:n_positive]
    positive_embedded_sub = positive_embedded[positive_indices,:]
    negative_indices = np.random.permutation(negative_embedded.shape[0])[0:n_negative]
    negative_embedded_sub = negative_embedded[negative_indices,:]
    neutral_indices = np.random.permutation(neutral_embedded.shape[0])[0:n_neutral]
    neutral_embedded_sub = neutral_embedded[neutral_indices,:]


    training_mat = np.concatenate([positive_embedded_sub, negative_embedded_sub, neutral_embedded_sub], axis=0)

    training_cases  = [positives[i] for i in positive_indices] + [negatives[i] for i in negative_indices] + [neutrals[i] for i in neutral_indices]
    #these are the cases that are actually used for training
    #return them in case they are useful for error analysis
    labels = np.array([0]*n_positive + [1]*n_negative + [2]*n_neutral)
    #labels for error analysis
    #will be equivalent to argmax of correct classifier output
    y = np.zeros([training_mat.shape[0], 3])
    #one-hot matrix for training
    y[0:n_positive,0] = 1
    y[n_positive:(n_positive + n_negative),1] = 1
    y[(n_positive + n_negative):,2] = 1

    if(hp["n_folds"]>=2):
        #first step:
        #use crossvalidation to estimate performance on hold-out data
        #the model versions trained here are not returned! they are discarded
        #keep only the predictions
        skf = StratifiedKFold(n_splits = hp["n_folds"], random_state = 33, shuffle=True)
        predictions = np.nan*np.ones([training_mat.shape[0], 3])
        #predictions made when the given data point was in holdout set

        for k, (train_indices, test_indices) in enumerate(skf.split(training_mat, labels)):
            print('\nTraining LSTM on fold %d / %d :\n'%(k+1, hp["n_folds"]))
            model = LSTM_graph(training_mat.shape[1], mapping)
            #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
            model.fit(training_mat[train_indices,:], y[train_indices,:],\
                      epochs=hp["n_epochs"], batch_size=hp["batch_size"], shuffle=True)
            predictions[test_indices,:] = model.predict(training_mat[test_indices,:])


    #now do not use crossvalidation
    #just train on all data provided
    #to obtain the final trained model, which is returned
    model = LSTM_graph(training_mat.shape[1], mapping)
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(training_mat, y, epochs=hp["n_epochs"], batch_size=hp["batch_size"], shuffle=True)

    #return a dict which includes both the model and extra data needed to run it
    model_dict = {"model":model, "max_len":max_len}

    #if we did not use crossvalidation, set the predictions to be predictions on training set
    if(hp["n_folds"] < 1):
        predictions = model.predict(training_mat)

    return (model_dict, predictions, labels, training_cases)

def predict_LSTM(model_dict, sentences, mapping):
    sentences = [string_to_printable_ascii(s) for s in sentences]
    return model_dict["model"].predict(embed_sentences(mapping, sentences, "index_matrix", model_dict["max_len"]))

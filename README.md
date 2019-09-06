# success or failure - a text classifier

In this project, I develop a classifier which can infer if an input text is describing an instance of success, an instance of failure, or neither.\
The classifier is an LSTM network which processes text that is transformed via GloVe word embeddings. I use web scraping, manual text selection and data augmentation techniques to accumulate a training dataset of > 10000 labeled example sentences, in total.\
As a real-world test case, I scrape a dataset from www.failory.com and run the classifier on it. This dataset consists of interviews with startup founders, which fall into two categories: the startup failed, or the startup succeeded (at least to the extent that it was still active at the time of interview). There are approximately 50 interviews in each category.\
(classifier final results here)
The entire project can be run from a single jupyter notebook, which is organized into sections that can be independently executed.


## The failory dataset

Failory.com has conducted interviews with a large number of startup founders, from a diverse set of business areas and countries. To get an idea of the scope of the dataset, this world map shows the home countries of all startups in the failory dataset:

![countries](map.png?raw=true "Map of startup home countries")



# success or failure - a text classifier

In this project, I develop a classifier which can infer if an input text is describing an instance of success, an instance of failure, or neither.\
The classifier is an LSTM network which runs on text that is transformed via GloVe word embeddings.\
As a real-world test case, I scrape a dataset from www.failory.com and run the classifier on it. This dataset consists of interviews with startup founders, which fall into two categories: the startup failed, or the startup succeeded (at least to the extent that it was still active at the time of interview). There are approximately 50 interviews in each category. (the classifier is able to...)

## The failory dataset

Failory.com has conducted interviews with a large number of startup founders, from a diverse set of business areas and countries. To get an idea of the scope of the dataset, this world map shows the home countries of all startups in the failory dataset:

![countries](map.png?raw=true "Map of startup home countries")



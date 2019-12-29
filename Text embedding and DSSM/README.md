Using a DSSM model for creating an embedding vector for each label(keyword) in the labels.csv file that can represent the label in the same semantic space.

1.The Embedding notebook uses an embedder trained on google-news30k weights for assigning a 1x300 size vector for each label.

2.Using these vectors a dataset is created word_dataset.csv having label name, class id it belongs to and the vector.

3.The TextClassifier notebook uses a DSSM model using LSTM for multilabel classification.After it is trained, each 1x300 vector is transorfmed into a 1x64 vector after taking output from the last hidden layer.

4.Using the vectors each keyword for an image is replaced with 10 closest similarity words.

4.The synonyms_corr.csv has corr coeff for each keyword.

5.Precision-synonyms_corr.csv contains overall precision.1000th row has avg precision.

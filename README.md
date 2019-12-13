Fusion of text and content based image retrieval.

Dataset used:
Wang 1k dataset having 10 image classes.

Steps:
1.Use Google Cloud Vision API for getting image labels.
2.Finiding correlation between labels and getting text based search accuracy.
3.Using Block Truncation Coding (BTC) and TSnBTC (Thepade's Sorted n-ary Block Truncation Coding) for getting color based features.
4.Using LBP for texture based features.
5.Using CNN to obatain a feature vector.
6.Trying various compbinations of feature vectors to get maximum accuracy.


The 'results.md' contains these results.
'main_files' contains code for btc, tsbctc, sift and for combination of feature vectors.
The 'CNN + Segementation' contains convolutional neural nework architecture for feature extraction.In it the wang_config_load contains implementation of Mask RCNN for a custom object.

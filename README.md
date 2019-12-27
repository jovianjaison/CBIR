### Fusion of query and context based image retrieval

### Dataset used:
  Wang 1k dataset having 10 image classes.

### Steps:
  1.Use Google Cloud Vision API for getting image labels.
  2.Finiding correlation between labels and getting text based search accuracy.
  3.Using Block Truncation Coding (BTC) and TSnBTC (Thepade's Sorted n-ary Block Truncation Coding) for getting color based    features.
  4.Using LBP for texture based features.
  5.Using CNN to obatain a feature vector.
  6.Trying various compbinations of feature vectors to get maximum accuracy.


### The 'results.md' contains these results.

### 'main_files' contains code for btc, tsbctc, sift and for combination of feature vectors.

### The 'CNN + Segementation' contains convolutional neural nework architecture for feature extraction.In it the wang_config_load contains implementation of Mask RCNN for a custom object.

### The 'csv_files' contains label data along with correlation and precision results.

### Features Employed for Image indexing:
 * Color
 * Shape
 * Texture
 * Spatial Relationships


### Color Spaces utilized:
 * RGB
 * kLUV
 * YCbCr
 * YUV


### Feature Extraction Methods Used:
 * Multilevel BTC
 * Multilevel TSnBTC
 * Fusion of BTC and TSnBTC



### Performance Evaluation parameters:
 * kaur2016_paper4
 	* Sensitivity
 	* Specificity
 	* Retrieval Score
 	* Error rate
 	* Accuracy



### Current Results:
 * TSnBTC-kLUV-n-17: 40.68 
 * BTC-kLUV-n-3: 41.64


### Fusion of TSnBTC and BTC
###### BTC-ColorSpace BTC-Level TSnBTC-Colorspace TSnBTC-n
 1.  kLUV 3  kLUV 17
 2. YCbCr 4  kLUV 14
 3. YCbCr 3  kLUV 16
 4.  kLUV 2  kLUV 11
 5.  kLUV 4  kLUV 21



### CBIR Systems:
 * MARS (employing feature weighting)
 * MindReader (employing complex feature weighting)
 * QCluster (employing probablistic models)
 * BlobWorld (System for region based Image Indexing and Retrieval)
 * VisualSeek 
 * NeTra (Toolbox for navigating large Image Databases)

### Ranking for SIFT:
	* As BFMatcher uses descriptor from 1st image and calculates euclidean distance with all descrriptors of 2nd image, then we can represent each descriptor on 128 dimensions. Then we can apply kNN to find what's the probability of that descriptor to belong to a particular image.
		* To use kNN we will use 128 bin arry as 128 features and image ID as label.
		* For every image find euclidean distance of every descriptor with every other descriptor in space.
		* Loop k from 1 - 10,000.
			* Get probabilities of every descriptor match with the query image.
			* Sort them in descending.
			* Select top 100.
			* Find Recall.
		* Plot graph of every recall vs k.
		* Select best k.
	* Content-Based_Image_Retrieval_using_SIFT


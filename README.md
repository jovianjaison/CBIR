### Fusion of query and context based image retrieval

### Dataset used:
  Wang 1k dataset having 10 image classes.
  https://drive.google.com/open?id=1dzywtP3PWx3PJcLfvZ_1K3i61Hcu3Ysp

### Steps:
  1.Use Google Cloud Vision API for getting image labels.
  
  2.Finiding correlation between labels and getting text based search accuracy.
  
  3.Using Block Truncation Coding (BTC) and TSnBTC (Thepade's Sorted n-ary Block Truncation Coding) for getting color based    features.
  
  4.Using LBP for texture based features.
  
  5.Using CNN to obatain a feature vector.
  
  6.Trying various compbinations of feature vectors to get maximum accuracy.


### The [RESULTS.md](RESULTS.md) contains all results.

### 'main_files' contains code for btc, tsbctc, sift and for combination of feature vectors.

### The 'CNN + Segementation' contains convolutional neural nework architecture for feature extraction.In it the wang_config_load contains implementation of Mask RCNN for a custom object.


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


### Feature Extraction Methods Used for content:
 * Multilevel BTC
 * Multilevel TSnBTC
 * Fusion of BTC and TSnBTC
 * Different CNN architectures 

### Feature Extraction Methods Used for text:
 * DSSM 

### Current BEST Results for CBIR using color and texture features:

Fusion of LBP with BTC and TSBTC:

| method 1     | method 2       | Acuuracy      | 
| :---         |     :---:      |          ---: |
| BTC3-LUV     | TSBTC3-LBP-LUV | 43.7%         |
| BTC3-LUV     | BTC2-LBP-LUV   | 42.64%        |
| TSBTC17-LUV  | TSBTC3-LBP-LUV | 42.1%         |
| TSBTC17-LUV  | BTC2-LBP-LUV   | 41.67%        |


### Current Results for CBIR using CNN:

| Architecture    | Acuuracy      | Merge Accuracy| 
| :---            | :---:         | :---:         |
| Conv-MaxPx2     | 84.86	  | 94.12         |
| Conv-MaxPx3     | 83.7	  | 92.59         |
| Conv-MaxPx4     | 84.01         | 93.44         |
| VGG             | 61.58  	  | 90.43         |
| Inveptionv3     | 30.93   	  | 90            |
| MobiNet         | 42.9   	  | 87.99         |
| ResNet50        | 32.11   	  | 90.05         |

Merge accuracy is combination of text and CNN based feature vectors

### Current Results for Label features:

| Technique                                          | Acuuracy      |  
| :---                                               | :---:         |   
| Using Api results                                  | 91.23	     |  
| 5 Top synonyms using DSSM for each api keyword     | 87.04	     | 
| 10 Top synonyms using DSSM for each api keyword    | 86.13         | 
| 20 Top synonyms using DSSM for each api keyword    | 82.15         | 


### CBIR Systems available today:
 * MARS (employing feature weighting)
 * MindReader (employing complex feature weighting)
 * QCluster (employing probablistic models)
 * BlobWorld (System for region based Image Indexing and Retrieval)
 * VisualSeek 
 * NeTra (Toolbox for navigating large Image Databases)




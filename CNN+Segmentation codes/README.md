Deep learning based approaches for content based feature retrieval

1.3xWang.ipynb notebook contains a simple 3 Convolution Maxpooling layer CNN.CNN was first trained and then used to extract features from ;ast hidden layer.

2.The VGG is a a notebook using VGG, Inceptionv3, Resnet50 and MobileNet architectures for the same above mentioned process.(These architectures haven't been re-trained on WANG dataset.That is yet to be done.)

3.The image_config notebook uses Mask-RCNN for image segmentaion on a cutom object.This helps eliminate background noise.(It worked well for classes with objects in them eg.dinosaur but failed in general images like beaches, mountains as it had no particular objects to detect.)

Drive links:

https://drive.google.com/drive/folders/19y70cpbhClRHyqiHI5fhw5-RVJFqfuER?usp=sharing
This is the link to helper files for MASK-RCNN

Results:
 1.3xCNN.csv, ResNet50.csv, VGG.csv,  are the feature vector obtained for each image(each row is vector for 1 image)
 
 2.3xCNNCorr.csv, VGGCorr.csv, ResNet50Corr.csv .Correlation coefficient is calculated to compare similarity between one image with all other images.
 
 3.Merge_ResNet50Corr.csv, Merge_VGGCorr .These correlation values are merged with correlation values obtained from labels.
 
 4.labels.csv, correlation-labels.csv, precision-labels.These are the labels obtained from the API call to cloud vision api.The second file is the correlation coeff for labels and third is the precision.The precision is calculated for eg treating image 1 and image 2 labels as different set, calculating the num of intersection elements divided by len of set a.
 
 5.Precision-3XCNNCorr, Precision-Merge_3xCNNCorr.csv,Precision-ResNet50Corr.csv, Precision-Merge_ResNet50Corr.csv, Precision-Merge_VGGCorr.csv, Precision-VGGCorr.csv As each class has 100 images the correlation vector for each image is sorted and how many of the top 100 belong to the class of the image gives precision.1000th row represents average precision.


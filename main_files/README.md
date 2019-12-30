## This folder contains code to extract content based features (`color` and `texture`).

### [Flowchart](Feature%20Extraction%20TSBTC.jpg) for Feature Extraction

### Steps:

1. Read image and separate image into color planes

2. Convert RGB to luminance chromaticity [color space](ColorSpace)(**K'LUV** and **YCbCr**)
	- [RGB to LUV](ColorSpace/kluv.py) is done using **Kekre's LUV** transform where **L** gives **luminance** and **U** and **V**
  gives **chromaticity** values of color image.
      ```
      L = R + G + B;
      U = -2*R + G + B + 510
      V = -G + B + 255
      ```
	
    - [RGB to YCbCr](ColorSpace/ycbcr.py) : **Y** gives **luminance** and **Cb** and **Cr** gives **chromaticity** values of colour image.
        ```
        Y = 0.2989*R + 0.5866*G + 0.1145*B
        Cb = -0.1688*R - 0.3312*G + 0.5000*B + 127.5
        Cr = 0.5000*R - 0.4184*G - 0.0816*B + 127.5
        ```
        
3. Extract features:
    - Color Features are extracted using **BTC(Block Truncation Coding)** and **TSBTC n-ary(Thepade's Sorted Block Truncation Coding)**.
    - **Texture Features** are extracted using **LBP(Local Binary Patterns)**.

* (a) [BTC](BTC) :
  - Block Truncation Coding(BTC) is a relatively simple image compression technique.
  - The method divides the image into its color planes and the mean intensity value of each color plane is calculated.
  - Further discussion is done considering the Red plane.
  - Next each pixel value is compared with the mean value and the image is divided into two regions : Lower Red and Upper Red.
  - Lower Red contains pixel values smaller than the mean value.
  - Upper Red contains pixel values greater than the mean value.
  - The mean value of these regions are added to the feature vector. Similar process is performed for Green and Blue plane.
  - BTC has been implemented upto 4 levels on [RGB](BTC/RGB/btc.py), [K’LUV](BTC/kLUV/btc.py) and [YCbCr](BTC/YCbCr/btc.py) color space.
  
* (b) [TSBTC n-ary](TSnBTC) :
	- faster and better image compression technique compared to BTC.
	- rotation and scale invariant.
	- Similar to BTC, here also image of size r x p is divided into different components, for eg. R, G and B component.
	- In TSBTC n-ary, every component is converted from a two dimensional array of size r x p into a Single Dimensional Array(SDA) of len r x p.
	- This SDA is then sorted and divided into n equal parts.
	- For every part, mean of all values in that part is calculated.
	- Vector of these mean values represents feature vector of that component.
	- Length of the feature vector for one component is equal to n.
	- Then, similar to BTC, feature vectors of all components are concatenated to get a final feature vector of size 3*n for that image.

  In this experiment, TSBTC n-ary was applied on 3 colorspaces, namely [RGB](TSnBTC/RGB/tsnbtc.py), [LUV](TSnBTC/kLUV/tsnbtc.py) and [YCbCr](TSnBTC/YCbCr/tsnbtc.py), with values for n ranging from n=2 to n=17.
  [Highest accuracy](../RESULTS.md) was observed for TSBTC 17-ary applied on LUV color space.

* (c) **LBP(Local Binary Patterns) :**
  - used to extract texture features.
	- LBP is one of the best texture descriptor methods which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
	- This binary number of each pixel is converted into decimal and stored in the feature vector.
	
	LBP has been implemented on different color spaces like [RGB](ColorSpace/rgb_lbp.py),K’LUV.
  
	Next [BTC](LBP-BTC) and [TSBTC](LBP-TSBTC) are implemented on LBP patterns to get texture features.

4. [Fusion](fusion-btc-tsnbtc):
	- **Joint** cosideration of **Color** and **Texture** features is under research and may yield better results.
	- Hence Color features from step **3(a)** and **3(b)** are combined with texture features from step **3(c)** to create a new feature vector.
  
### Folder Structure main_files/:
  - [ColorSpace](ColorSpace) - code for converting image from one color space to another
  - [ColorSpace/rgb_lbp.py](ColorSpace/rgb_lbp.py) - code to find lbp patterns
  - [BTC/](BTC)
    - [RGB/btc.py](BTC/RGB/btc.py) - code for applying BTC on RGB color space 
    - [YCbCr/btc.py](BTC/YCbCr/btc.py) - code for applying BTC on YCbCr color space
    - [kLUV/btc.py](BTC/kLUV/btc.py) - code for applying BTC on LUV color space
  - Similar structure for [TSnBTC](TSnBTC)
  - [LBP-BTC](LBP-BTC) - code to extract texture features by applying BTC on LBP patterns  
  - [LBP-TSBTC](LBP-TSBTC) - code to extract texture features by applying TSBTC n-ary on LBP patterns
  - [fusion-btc-tsnbtc](fusion-btc-tsnbtc) - code to combine btc and tsbtc features
  
  
  
  
  

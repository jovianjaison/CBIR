# All Results
### Results for Wang 1K
 * TSnBTC
	* RGB
		*  2: 39.11
		*  3: 39.323
		*  4: 39.235
		*  5: 39.294
		*  6: 39.318
		*  7: 39.305
		*  8: 39.355
		*  *9: 39.369*
		* 10: 39.353
		* 11: 39.342
		* 12: 39.361
		* 13: 39.356
		* 14: 39.358
		* 15: 39.361
		* 16: 39.36
		* 17: 39.349
		* 18: 39.356
		* 19: 39.352
		* 20: 39.348
		* 21: 39.354
		* 22: 39.348
		* 23: 39.353
		* 24: 39.347
	* YCbCr
		*  2: 38.897
		*  3: 39.363
		*  4: 39.525
		*  5: 39.731
		*  6: 39.728
		*  7: 39.72
		*  8: *39.768*
		*  9: 39.757
		* 10: 39.745
		* 11: 39.735
		* 12: 39.751
		* 13: 39.735
		* 14: 39.741
		* 15: 39.757
		* 16: 39.761
		* 17: 39.773
		* 18: 39.761
		* 19: 39.773
		* 20: 39.775
		* 21: 39.78
		* 22: 39.773
		* 23: 39.77
		* 24: 39.773
	* kLUV
		*  2: 39.512
		*  3: 40.158
		*  4: 40.362
		*  5: 40.54
		*  6: 40.608
		*  7: 40.6
		*  8: 40.652
		*  9: 40.667
		* 10: 40.663
		* 11: 40.674
		* 12: 40.666
		* 13: 40.668
		* 14: 40.679
		* 15: 40.67
		* 16: 40.678
		* 17: *40.68*
		* 18: 40.669
		* 19: 40.665
		* 20: 40.66
		* 21: 40.672
		* 22: 40.66
		* 23: 40.668
		* 24: 40.667

 * BTC
	* RGB
		*  1: 37.27
		*  2: 38.51
		*  3: *39.18*
		*  4: 37.24
	* YCbCr
		*  1: 38.29
		*  2: 40.35
		*  3: 41.14
		*  4: *41.22*
	* kLUV
		*  1: 38.321
		*  2: 40.93
		*  3: **41.64**
		*  4: 40.69

 * Fusion of TSnBTC and BTC
	###### BTC-ColorSpace BTC-Level TSnBTC-Colorspace TSnBTC-n
	 1.  kLUV 3  kLUV 17 : *41.559*
	 2. YCbCr 4  kLUV 14 : 40.928
	 3. YCbCr 3  kLUV 16 : 40.797
	 4.  kLUV 2  kLUV 11 : 41.335
	 5.  kLUV 4  kLUV 21 : 41.5

 * Spatial BTC (2x2):
	1. kLUV
		* 1 : 28.26
		* 2 : 30.444
		* 3 : 31.007
		* 4 : 30.741

 * Spatial TSnBTC (2x2):
		* 17 : 40.429

 * LBP RGB
	1. BTC: 
		* Level=1: 29.118
		* Level=2: 28.061
		* Level=3: 26.651
		* Level=4: *30.016*

	2. TSnBTC: 
		* n =  2: 28.662
		* n =  3: 27.979
		* n =  4: 29.083
		* n =  5: 29.102
		* n =  6: 29.132
		* n =  7: 29.389
		* n =  8: 29.428
		* n =  9: 29.419
		* n = 10: 29.373
		* n = 11: 29.403
		* n = 12: *29.434*
		* n = 13: 29.381
		* n = 14: 29.42
		* n = 15: 29.39
		* n = 16: 29.42
		* n = 17: 29.402
 
 * LBP kLUV
	1. BTC: 
		* Level=1: 35.416
		* Level=2: *36.676*
		* Level=3: 35.78
		* Level=4: 34.966

	2. TSnBTC: 
		* n =  2: 34.062
		* n =  3: *35.282*
		* n =  4: 35.047
		* n =  5: 35.136
		* n =  6: 34.891
		* n =  7: 34.794
		* n =  8: 34.768
		* n =  9: 34.787
		* n = 10: 34.724
		* n = 11: 34.695
		* n = 12: 34.691
		* n = 13: 34.562
		* n = 14: 34.585
		* n = 15: 34.592
		* n = 16: 34.526
		* n = 17: 34.577

 * Fusion of BTC methods applied directly on image and applied on LBP patterns:
 	* LUV_3_LBP_LUV_2	: 42.644
 	* YCbCr_4_LBP_LUV_3	: 40.062
 	* YCbCr_3_LBP_LUV_1 : 41.895

 * Fusion of LBP_RGB_BTC_4 & BTC_kLUV_3: 42.306
 
 * FUSION of LBP with BTC and TSnBTC:
 	* BTC_kLUV_3:
		* BTC_LBP_2    : 42.644
		* TSnBTC_LBP_3 : *43.697*
	* TSnBTC_kLUV_17:
		* BTC_LBP_2    : 41.669 
		* TSnBTC_LBP_3 : 42.095

 * SIFT-SIFT  : 
 * SIFT-FREAK :

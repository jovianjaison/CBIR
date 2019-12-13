import numpy as np
from pandas import DataFrame
from multiprocessing import Pool
from skimage.feature import local_binary_pattern
import os
import cv2

class ColorSpace:

	def __init__(self, images):
		self.color_space_divisions_for_all_images = dict()
		self.name = 'ColorSpace'
		self.images = images
		self.lbp = False
		self.radius = 1
		self.n_points = 8 * self.radius
		self.METHOD = 'default'
		self.save_folder = '../csv/ColorSpace'
		if not os.path.exists(self.save_folder): os.makedirs(self.save_folder)


	def set_lbp(self, value):
		self.lbp = value


	# Add LBP function
	def get_lbp_values(self, colors):
		lbp_colors = []
		for color in colors:
			lbp_colors.append(local_binary_pattern(colors, self.n_points, self.radius, self.METHOD))

		return lbp_colors


	def color_space_division(self, img, colourSpace):
		colors = []
		# separate img into RGB plane
		for i in range(2, -1, -1):
			colors.append(img[:,:,i])

		if self.lbp:
			colors = self.get_lbp_values(colors)

		colors = [np.hstack(x) for x in colors]
		R, G, B = colors

		if(colourSpace == "RGB"):
			#R, G, B = np.sort(R), np.sort(G), np.sort(B) 
			return R, G, B

		elif(colourSpace == "LUV"):
			#this is Kekre's LUV or KLUV
			L = R + G + B;
			U = -2*R + G + B + 510
			V = -G + B + 255
			
			# this is CIE LUV
			#img_luv = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
			#colors = []
			#for i in range(3):
			#	colors.append(np.hstack(img_luv[:, :, i]))
			#L, U, V = colors

			#L, U, V = np.sort(L), np.sort(U), np.sort(V)
			print('L:', U)
			print('R:', R)
			print('G:', G)
			print('B:', B)
			return L, U, V

		elif(colourSpace == "YCbCr"):
			#Y = 0.2989*R + 0.5866*G + 0.1145*B
			#Cb = -0.1688*R - 0.3312*G + 0.5000*B + 127.5
			#Cr = 0.5000*R - 0.4184*G - 0.0816*B + 127.5
			img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
			colors = []
			for i in range(3):
				colors.append(np.hstack(img_ycrcb[:, :, i]))

			Y, Cr, Cb = colors
			#Y, Cb, Cr = np.sort(Y), np.sort(Cb), np.sort(Cr)
			return Y, Cb, Cr


	def color_spaces_for_all_images(self, color_space):
		if self.lbp: LBP = "_LBP"
		else: LBP = ""
		color_space_values = np.array([self.color_space_division(img, color_space) for img in self.images])
		print(color_space_values.shape)
		#print(len(self.color_space_divisions_for_all_images))
		return (color_space+LBP, color_space_values)


	def get_all_color_spaces(self, color_spaces):
		print('IN get_all_color_spaces')
		#with Pool() as pool:
		#	color_spaces_for_all_images = pool.map(self.color_spaces_for_all_images, [color_space for color_space in color_spaces])

		for color_space in color_spaces:
			temp = self.color_spaces_for_all_images(color_space)
			self.color_space_divisions_for_all_images[temp[0]] = temp[1]
		#print(type(color_spaces_for_all_images))
		#print(type(color_spaces_for_all_images[0]))

	def save_color_space_to_csv(self):
		for color_space, color_space_values in self.color_space_divisions_for_all_images.items():
			save_folder = os.path.join(self.save_folder, color_space)
			if not os.path.exists(save_folder):
				os.makedirs(save_folder)
			for i in range(len(color_space_values)):
				df = DataFrame(color_space_values[i])
				df.to_csv(os.path.join(save_folder, str(i)+'.csv'))

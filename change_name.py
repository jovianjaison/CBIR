import os
import cv2

class Change_Name():
	def __init__(self):
		self.read_folder = "../dataset/test1/image.orig/"
		self.SAVE_FOLDER = "../dataset/test1-renamed"
		self.files = sorted(os.listdir(self.read_folder))

	def change_name(self, filename):
		if len(filename) == 5: return "00" + filename
		elif len(filename) == 6: return "0" + filename
		else: return filename

	def write_with_new_name(self):
		if not os.path.exists(self.SAVE_FOLDER):
			os.makedirs(self.SAVE_FOLDER)
		for i in self.files:
			cv2.imwrite(os.path.join(self.SAVE_FOLDER, self.change_name(i)), cv2.imread(os.path.join(self.read_folder, i)))

		#return self.SAVE_FOLDER




import numpy as np 
import time
from multiprocessing import Pool, Process
from math import ceil
import pickle
import os

class TSBTC:
	def __init__(self):
		self.feature_color_space_wise = dict()
		self.save_folder = os.path.join('csv', 'TSBTC')
		self.name = 'TSBTC'


	def tsbtc(self, arr, lvl):
		step = ceil(len(arr) / (lvl*2))
		arr = np.sort(arr)
		features = [ np.mean(arr[i : i+step]) for i in range(0, len(arr), step) ]
		return features


	def tsbtc_lvl_wise(self, lvl, color_space_divisions):
		temp = []
		for img in color_space_divisions:
			temp.append([self.tsbtc(j, lvl) for j in img])

		with open(str(lvl)+'.pkl', 'wb') as op:
			pickle.dump(temp, op)

	def get_features(self, argx):
		levels, color_space_name, color_space_divisions = argx
		features_lvl_wise = dict()
		#with Pool() as pool:
		#	temp = pool.map(self.tsbtc_lvl_wise, [(lvl, color_space_divisions) for lvl in levels])

		pool = []
		for lvl in levels:
			pool.append(Process(target=self.tsbtc_lvl_wise, args=((lvl, color_space_divisions))))
			pool[-1].start()

		for p in pool: p.join()

		for k in levels:
			with open(str(k)+'.pkl', 'rb') as ip:
				features_lvl_wise[k] = pickle.load(ip)

		self.feature_color_space_wise[color_space_name] = features_lvl_wise
		print(f'Completed {self.name} {color_space_name}')


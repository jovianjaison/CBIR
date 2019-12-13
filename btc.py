import pickle
import numpy as np 
from bisect import bisect_left
from queue import Queue
from multiprocessing import Pool, Process
from re import findall
from python_files.helper import convert_to_df
from collections import defaultdict
from pandas import DataFrame
from pandas import Series
import os

class BTC:
	def __init__(self):
		self.feature_color_space_wise = dict()
		self.levels = 0
		self.save_folder = os.path.join('csv', 'BTC')
		self.name = 'BTC'


	def divide(self, arr, mean):
		i = bisect_left(arr,mean)
		lower = arr[:i]
		upper = arr[i:]
		return (lower,np.mean(lower)), (upper,np.mean(upper))

	def btc(self, arr):
		q = Queue()
		q.queue.clear()
		features_lvl_wise = dict()

		q.put((arr, np.mean(arr)))
		for i in self.levels:
			loop_condition = q.qsize()
			temp = []
			#print(i)
			for j in range(loop_condition):
				arr, mean = q.get()
				lower_with_mean, upper_with_mean = self.divide(arr, mean)
				temp.append(lower_with_mean[1])
				temp.append(upper_with_mean[1])
				q.put(lower_with_mean)
				q.put(upper_with_mean)
			features_lvl_wise[i] = temp

		q.queue.clear()
		#print(len(features_lvl_wise[1]))
		return features_lvl_wise  #all levels for one image

	def btc_color_wise(self, color, color_space_values):
		features_lvl_wise = defaultdict(list)
		#print(type(color_space_values))
		#print(color)
		for img in color_space_values:
			#print(type(img))
			temp_features_level_wise = self.btc(img[color])
			for k, v in temp_features_level_wise.items():
				features_lvl_wise[k].append(v)

		with open(str(color)+'.pkl', 'wb') as op:
			pickle.dump(features_lvl_wise, op)
		#return 1 #all levels for all images and one color


	def get_features(self, argx):
		print('In get_features')
		self.levels, color_space_name, color_space_values = argx
		features_color_wise = dict()
		colors = findall('[A-Z][^A-Z]*', color_space_name)
		#print(colors)
		pool = []
		#with Pool() as pool:
		#	temp = pool.map(self.btc_color_wise, [(index, color_space_values) for index, color in enumerate(colors)])

		for index, color in enumerate(colors):
			pool.append(Process(target=self.btc_color_wise, args=((index, color_space_values))))
			pool[-1].start()
			print(pool[-1].is_alive())

		for i in pool:
			i.join()
			print(i.is_alive())

		for i in range(len(colors)):
			with open(str(i)+'.pkl', 'rb') as ip:
				features_color_wise[colors[i]] = pickle.load(ip)

		self.feature_color_space_wise[color_space_name] = features_color_wise
		print(f'Completed {self.name} {color_space_name}')


	def rearrange_feature_dict(self):
		for color_space, features_color_wise in self.feature_color_space_wise.items():
			temp = defaultdict(DataFrame)
			for color, features_lvl_wise in features_color_wise.items():
				for lvl, features in features_lvl_wise.items():
					temp[lvl][color] = Series(features)
			self.feature_color_space_wise[color_space] = temp



#!/usr/bin/env python3

import numpy as np
import os
import cv2
import pandas as pd
from collections import defaultdict
from joblib import dump, load
from math import ceil


def btc_divide(arr, lvl):
	if len(arr) == 0: mean = 0
	else: mean = sum(arr)/len(arr)
	if lvl == 0:
		return [mean]
	else:
		arr1 = [x for x in arr if x < mean]
		arr2 = [x for x in arr if x >= mean]
		results = []
		results.extend(btc_divide(arr1, lvl-1))
		results.extend(btc_divide(arr2, lvl-1))

		return results


def divide_image(mat):
	col_stride = len(mat)//2
	row_stride = len(mat[0])//2
	ret = []
	for i in range(0, len(mat), col_stride):
		temp = mat[i:i+col_stride]
		parts = defaultdict(list)
		for row in temp:
			stride = len(row)//2
			for x in range(0, len(row), row_stride):
				parts[x//stride].extend(row[x:x+row_stride])
		ret.extend(list(parts.values()))
	return ret



def btc_luv(l, u, v, lvl):
	results = []
	
	parts_l = divide_image(l)
	parts_u = divide_image(u)
	parts_v = divide_image(v)
	#print(len(parts_l[0]))

	
	for j in (parts_l, parts_u, parts_v):
		temp = []
		for i in parts_l:
			temp.append(btc_divide(i, lvl))

		for i in range(len(temp[0])):
			feature = 0
			for j in range(len(temp)):
				feature += temp[j][i]
			feature = feature/len(temp)
			results.append(feature)


	return results


def mse(df):
	results = []

	for i in range(df.shape[0]):
		temp = []
		for j in range(df.shape[0]):
			base = df.iloc[i, :]
			query = df.iloc[j, :]
			ans = []
			for x in range(len(base)):
				ans.append((base[x] - query[x])**2)

			temp.append(sum(ans)/len(ans))

		results.append(temp)

	results = pd.DataFrame(results)

	return results

def get_recall(df):
	results = []
	for i in range(df.shape[0]):
		base = df.iloc[i, :]
		base = base.sort_values()[:100].index.tolist()
		count = 0
		for b in base:
			if b//100 == i//100:
				count += 1

		results.append(count)

	return results

if __name__=='__main__':
	df = load('kluv-matrixed.pkl')

	print('\n', '-'*60, 'kLUV_MATRIXED', '-'*60, '\n')
	print(df.head())
	print(df.shape)
	
	for n in range(1, 5, 1):
		results = []
		features = []
		print('\n', '-'*60, n, '-'*60, '\n')
		if 'SPATIAL_BTC_' + str(n) + '.pkl' not in os.listdir():
			for j in range(df.shape[0]):
				features.append(btc_luv(df.iloc[j, 0], df.iloc[j, 1], df.iloc[j, 2], n))
				print(f'Image {j} done')
			features = pd.DataFrame(features)
			dump(features, 'SPATIAL_BTC_' + str(n) + '.pkl')
			print(features.head())
			print(features.shape)
		else:
			features = load('SPATIAL_BTC_'+str(n) + '.pkl')

		if 'SIMILARITY_MATRIX_' + str(n) + '.pkl' not in os.listdir():
			similarity_df = mse(features)
			dump(similarity_df, 'SIMILARITY_MATRIX_' + str(n) + '.pkl') 
			print('\n', '-'*30, 'SIMILARITY_MATRIX', '-'*30, '\n')
			print(similarity_df.head())
			print(similarity_df.shape)
		else:
			similarity_df = load('SIMILARITY_MATRIX_' + str(n) + '.pkl')


		if 'RECALL_' + str(n) + '.pkl' not in os.listdir():
			recall = get_recall(similarity_df)
			dump(recall, 'RECALL_' + str(n) + '.pkl')
		else:
			recall = load('RECALL_' + str(n) + '.pkl')

		print()
		print('*'*150)
		print()
		print('AVERAGE RECALL FOR ' + str(n) + ':', sum(recall)/len(recall))
		print()
		print('*'*150)
		print()

#!/usr/bin/env python3

import cv2
import numpy as np
import os
import joblib
import pandas as pd

OUTPUT = ""

detector = cv2.xfeatures2d.SIFT_create()
descriptor = cv2.xfeatures2d.SIFT_create()
matcher = cv2.BFMatcher()

def get_keypoints(img):
	ret = detector.detect(img, None)
	return ret

def get_descriptors(img, kps):
	_, des = descriptor.compute(img, kps)
	return des

def get_euclidean_dist(df):
	ret = np.zeros((len(df), len(df)))
	for i in range(len(df)):
		for j in range(i, len(df)):
			q = df.iloc[i, 1:]
			p = df.iloc[j, 1:]
			ans = 0
			for x in range(len(p)):
				ans += (q[x] - p[x])**2
			ans = ans**0.5
			ret[i,j] = ret[j,i] = ans
		print(f'Descriptor {i} done')
	ret = pd.DataFrame(ret)
	return ret

def get_similarity_percentage(des1, des2):
	matches = matcher.knnMatch(des1, des2, k=2)

	#Applying Lowe's ratio test
	ret = []
	for m, n in matches:
		if m.distance/n.distance < 0.8:
			ret.append(m)

	return ret

def get_similarity_matrix(des_df):
	ret = []
	for k1, v1 in des_df.items():
		matches = []
		for k2, v2 in des_df.items():
			matches.append(get_similarity_percentage(v1, v2))
		ret.append(matches)

	return ret

def get_probability(count, n):
	ret = {}
	for k, v in count.items():
		ret[k] = v/n
	return ret

def get_probability_of_all_des(df, labels, k):
	ret = []
	for i in range(len(df)):
		q = df.iloc[i, :]
		q = q.sort_values(ascending=True, inplace=False)[:k]
		count = {}
		print(q)
		for j in labels.unique():
			count[j] = 0
		for j in q.index:
			print(j)
			count[labels[j]] += 1
		ret.append((i, get_probability(count, k)))
	return ret


def get_recall(prob, labels, n):
	ret = []
	x = np.zeros((n, n))
	count = 0
	for i, v in prob:
		index = labels[i]
		if i == 0: count = 0
		elif index == labels[i-1]: count += 1
		else:
			for j in range(n):
				x[labels[i-1]][j] = x[labels[i-1]][j]/count
			count = 0
		for j in range(n):
			x[index][j] += v[j]

	for i in range(n):
		q = x[i]
		q.sort()
		print(q)
		temp = q.tolist()[:100]
		temp = [j for j in temp if j//100 == i//100]
		ret.append(len(temp))

	return ret

if __name__ == "__main__":
	#IMG_FOLDER = "/home/rohan/Personal/College-work/BE Proj/BEProject/dataset/test1-renamed"
	IMG_FOLDER = "/mnt/disks/disk_1/be-project/dataset/test1-renamed"
	files = sorted(os.listdir(IMG_FOLDER))

	images = {}
	keypoints = {}
	des_df = []

	min_kps = 10000
	if 'keypoints.csv' not in os.listdir() or 'descriptors_dataset.csv' not in os.listdir():
		for f in files:
			if '.jpg' in f:
				img = cv2.imread(os.path.join(IMG_FOLDER, f))
				index = int(f.split('.')[0])
				images[index] = img
				keypoints[index] = get_keypoints(img)
				if min_kps > len(keypoints[index]): min_kps= len(keypoints[index])
				des = get_descriptors(img, keypoints[index])
				for i in range(len(des)):
					des_df.append([index, des[i]])
				print(f'Image {index} done')
				
		OUTPUT += f'Minimum number of keypoints is {min_kps}\n'
		keypoints = pd.DataFrame.from_dict(keypoints, orient='index')
		keypoints.to_csv('keypoints.csv')

		des_df = pd.DataFrame(des_df)
		des_df.columns = ['label', 'des']
		des_df[['feature_'+str(i) for i in range(len(des_df.iloc[0, 1]))]] = pd.DatFrame(des_df.des.values.tolist(), index=des_df.index)
		des_df = des_df.drop('des', axis=1)
		print(des_df.head())
		print(des_df.shape)
		des_df.to_csv('descriptors_dataset.csv', index=False)

	else:
		keypoints = pd.read_csv('keypoints.csv', index_col='Unnamed: 0')
		des_df = pd.read_csv('descriptors_dataset.csv')

	euclidean_dist_df = get_euclidean_dist(des_df)
	euclidean_dist_df.to_csv('euclidean_distance.csv', index=False)

	labels_df = des_df.loc[:, 'label']
	
	for i in range(100, 1000):
		prob = get_probability_of_all_des(euclidean_dist, labels_df, i)
		recall = get_recall(prob, labels_df, )
		print('*'*60, f'\nAverage Recall for k={i} is {sum(recall)/len(recall)}\n', '*'*60)
		joblib.dump('RECALL_'+str(i), recall)

	'''
	matches_matrix = get_similarity_matrix(descriptors)
	recall = get_recall(matches_matrix)
	'''

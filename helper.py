import os
import cv2
import pandas as pd
import numpy as np
from re import findall
import pickle
from multiprocessing import Pool

def convert_to_df(features, color_space, lvl, tsbtc):
	features = pd.DataFrame(features)

	#    print(features.columns) 
	#    return features
	if tsbtc:
		step = lvl*2
		columns = np.arange(3, 3 + (step*3))
	else:
		step = 2**lvl
		columns = create_column_names(findall('[A-Z][^A-Z]*', color_space), lvl)
	indices = 0
	#if step == 1: return features
	for i in range(0, len(columns), step):
		features[columns[i:i+step]] = pd.DataFrame(features.iloc[:, indices].values.tolist(), index=features.index)
		indices += 1
	features = features.iloc[:, 3: ]
	#print(features.shape)
	#print(features.columns)

	return features


def read_all_images(folder, extension):
	files = os.listdir(folder)
	files.sort()
	images = []
	for file in files:
		if extension in file:
			images.append(cv2.imread(os.path.join(folder, file)))

	return images

# function to create column names for each level
def create_column_names(cols, no_of_levels):
	if(no_of_levels == 0):
		return cols
	else:
		col = []
		for c in cols:
			col.append("lower_"+c)
			col.append("upper_"+c)
		return create_column_names(col,no_of_levels-1)



def get_features_for_all_color_spaces(color_space_divisions_for_all_images, levels, algo):
	for color_space, color_space_divisions in color_space_divisions_for_all_images.items():
		algo.get_features((levels, color_space, color_space_divisions))

	#
	#for k, v in color_space_features:
	#	algo.feature_color_space_wise[k] = v
	if algo.name == 'BTC': algo.rearrange_feature_dict()

	#return feature_color_space_wise


def get_labels():
	filename = input('Enter name of labels dataset: ')
	df = pd.read_csv(filename, index_col='ID', encoding="ISO-8859-1")
	df = df.loc[:,['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9', 'label10', ]]

	print(df)
	df.to_csv(os.path.join('csv', 'labels-only-' + filename))


def save_features(feature_color_space_wise, main_folder):
	for color_space, features_lvl_wise in feature_color_space_wise.items():
		for lvl, features in features_lvl_wise.items():
			save_folder = os.path.join(main_folder, color_space, 'Level'+str(lvl))
			print(save_folder)
			if not os.path.exists(save_folder):
				os.makedirs(save_folder)
			features = convert_to_df(features, color_space, lvl, 'TSBTC' in main_folder)
			features.to_csv(os.path.join(save_folder, "Level" + str(lvl) + ".csv"), index=False)

def save_object(obj):
	#if not os.path.exists(obj.save_folder):
	#	os.makedirs(obj.save_folder)
	filename = os.path.join('pkl', obj.name + ".pkl")
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output)

def load_object(filename):
	with open(filename, 'rb') as p:  # Overwrites any existing file.
		obj = pickle.load(p)

	return obj

import pandas as pd
import os
from multiprocessing import Process
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def hpc(dir_path, m, cs, f):

	path = os.path.join(dir_path,m,cs,f[:6],f)
	# path = dir_path + m + "/" + cs + "/" + f
	corr_path = os.path.join(dir_path,m,cs,f[:6],f.split(".")[0]+"_MATCH_PERCENT.csv")
	# corr_path = dir_path + m + "/" + cs + "/" + f.split(".")[0] + "Corr.csv"
	
	# read csv
	df = pd.read_csv(path)
	df[:] = np.nan_to_num(df)

	# take transpose
	#df = df.T
	
	# calculate correlation
	#corr = df.corr()
	
	# convert decimal to percentage
	#corr = corr.mul(100)


	
	corr = [0]*df.shape[0]

	for i in range(df.shape[0]):
		#print(i)
		temp = pd.DataFrame([list(df.iloc[i, :])]*df.shape[0])
		corr[i] = list(mean_squared_error(df.T,temp.T, multioutput='raw_values'))
	
	'''
		for j in range(i, df.shape[0]):
			ans = mean_squared_error(df.iloc[i, :], df.iloc[j, :])
			corr[i][j] = corr[j][i] = ans
	'''
	#corr = euclidean_distances(df,df)

	corr = pd.DataFrame(corr)	
	# write into csv
	corr.to_csv(corr_path)
	print(corr_path + '\tDone')

def run():
	filenames = ['Level1.csv','Level2.csv','Level3.csv','Level4.csv','Level5.csv']
	method = ['BTC','TSBTC']
	colour_spaces = ['RGB','LUV','YCbCr']
	dir_path = "csv"
	processes = []

	for m in method:
		for cs in colour_spaces:
			for f in filenames:
				processes.append(Process(target=hpc, args=((dir_path, m, cs, f))))
				processes[-1].start()

	for i in processes:
		if i.is_alive():
			i.join()
    

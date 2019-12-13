from multiprocessing import Process
import pandas as pd
import os

def hpc(dir_path, m, cs, f):
	path = os.path.join(dir_path,m,cs,f[:6],f)
	precision_path = os.path.join(dir_path,m,cs,f[:6],"Precision" + f[5] + ".csv")

	df = pd.read_csv(path,index_col = 0)

	def sort_acc(val):
		return val[1]

	precision = []

	for x in range(len(df)):
		temp1 = df.loc[x,:]
		temp2 = [(i,j) for i,j in enumerate(temp1)]
		temp2.sort(key=sort_acc)
		temp2 = temp2[:100]
		temp3 = [i for i, j in temp2 if i // 100 == x // 100]
		precision.append(len(temp3))

	avg = round(sum(precision)/len(precision), 2)
	precision.append(avg)
	print('\t\t', f[:6])
	precision_df = pd.DataFrame(precision)
	print("\t\t\tAvg : ",avg)
	precision_df.to_csv(precision_path)

def run():
	filenames = ['Level1_MATCH_PERCENT.csv','Level2_MATCH_PERCENT.csv','Level3_MATCH_PERCENT.csv','Level4_MATCH_PERCENT.csv','Level5_MATCH_PERCENT.csv',]
	#filenames = ['Level1EUC_DIST.csv', 'Level2EUC_DIST.csv', 'Level3EUC_DIST.csv', 'Level4EUC_DIST.csv', 'Level5EUC_DIST.csv', ]
	method = ['BTC','TSBTC']
	colour_spaces = ['RGB','LUV','YCbCr']
	dir_path = "csv"
	processes = []
	for m in method:
		print(m)
		for cs in colour_spaces:
			print('\t', cs)
			for f in filenames:
				processes.append(Process(target=hpc, args=((dir_path, m, cs, f))))
				processes[-1].start()

	for i in processes:
		if i.is_alive(): i.join()

	Levels = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5']
	algo = dict()
	for m in method:
		print(m)
		cs_dict = dict()
		for cs in colour_spaces:
			print('\t', cs)
			level_dict = dict()
			for lvl in Levels:
				files = os.listdir(os.path.join(dir_path, m, cs, lvl))
				f = files.index('Precision'+lvl[-1]+'.csv')
				level_dict[int(lvl[-1])] = pd.read_csv(os.path.join(dir_path, m, cs, lvl, files[f])).at[1000, '0']

			cs_dict[cs] = level_dict

		algo[m] = cs_dict

	return algo

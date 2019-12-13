import pandas as pd
import numpy as np


class CompareLabels:

	def __init__(self, filename):
		self.filename = filename
		self.get_matching_percentage()
		self.save_acc_df()

	def get_unique_labels_with_index(self, df):

		labels = tuple(set(df.values.ravel().tolist()))
		label_to_num = {j:i for i, j in enumerate(labels) if j is not None}

		print(f'Vocab: {len(labels)}')

		return label_to_num


	def convert_rows_to_set(self, df, label_to_num):

		df = df.replace(label_to_num)
		set_df = []
		for i in range(len(df)):
			set_df.append(set(df.loc[i]))

		return set_df


	def get_matching_percentage(self):
		df = pd.read_csv(self.filename, index_col='ID')
		label_to_num = self.get_unique_labels_with_index(df)
		set_df = self.convert_rows_to_set(df, label_to_num)

		df_label_series = pd.Series(set_df)

		self.accuracy_df = pd.DataFrame(np.zeros((len(df_label_series), (len(df_label_series)))))

		for i in range(len(df_label_series)):
			self.accuracy_df[i][i] = 100
			len_i = len(df_label_series[i])

			for j in range(i+1, len(df_label_series)):
				len_j = len(df_label_series[j])

				if len_i != 0:
					self.accuracy_df[i][j] = round((len_i - len(df_label_series[i] - df_label_series[j])) / len_i * 100, 2)
				else:
					self.accuracy_df[i][j] = 0

				if len_j != 0:
					self.accuracy_df[j][i] = round((len_j - len(df_label_series[j] - df_label_series[i])) / len_j * 100, 2)
				else:
					self.accuracy_df[j][i] = 0


	def save_acc_df(self):
		self.accuracy_df.index.name = 'ID'
		print(self.accuracy_df)
		self.accuracy_df.to_csv('matching-percentage-' + self.filename)



		
		


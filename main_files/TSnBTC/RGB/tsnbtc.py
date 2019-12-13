#!/usr/bin/env python3

import numpy as np
import os
import cv2
import pandas as pd
from collections import defaultdict
from joblib import dump, load
from math import ceil


def tsbtc_n_ary_luv(l, u, v, n):
    l = np.sort(np.array(l))
    u = np.sort(np.array(u))
    v = np.sort(np.array(v))

    step = ceil(len(l) / n)
    feature_l, feature_u, feature_v = [], [], []
    for i in range(0, len(l), step):
        feature_l.append(sum(l[i:i+step])/len(l[i:i+step]))
        feature_u.append(sum(u[i:i+step])/len(u[i:i+step]))
        feature_v.append(sum(v[i:i+step])/len(v[i:i+step]))

    results = []
    results.extend(feature_l)
    results.extend(feature_u)
    results.extend(feature_v)

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
    
    df = load('../../ColorSpace/rgb.pkl')

    print('\n', '-'*60, 'RGB', '-'*60, '\n')
    print(df.head())
    print(df.shape)
    for i in range(2, 17, 1):
        n = i
        results = []
        features = []
        print('\n', '-'*60, n, '-'*60, '\n')
        if 'TSnBTC' + str(n) + '.pkl' not in os.listdir():
            for j in range(df.shape[0]):
                features.append(tsbtc_n_ary_luv(df.iloc[j, 0], df.iloc[j, 1], df.iloc[j, 2], n))
            features = pd.DataFrame(features)
            dump(features, 'TSnBTC' + str(n) + '.pkl')
            print(features.head())
            print(features.shape)
        else:
            features = load('TSnBTC' + str(n) + '.pkl')

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
 

#!/usr/bin/env python3

import numpy as np
import pandas as pd
from joblib import dump, load
import os

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


if __name__ == '__main__':

    features_btc = load('BTC3.pkl')
    features_tsnbtc = load('TSnBTC17.pkl')
    
    features = pd.concat([features_btc, features_tsnbtc], axis=1, sort=False)
    features.columns = [i for i in range(features_btc.shape[1] + features_tsnbtc.shape[1])]

    print('-'*60 + 'BTC' + '-'*60)
    print(features_btc.head())
    print(features_btc.shape)

    print('-'*60 + 'TSnBTC' + '-'*60)
    print(features_tsnbtc.head())
    print(features_tsnbtc.shape)

    print('-'*60 + 'Fusion' + '-'*60)
    print(features.head())
    print(features.shape)
    
    if 'SIMILARITY_MATRIX.pkl' not in os.listdir():
        similarity_df = mse(features)
        dump(similarity_df, 'SIMILARITY_MATRIX.pkl') 
        print('\n', '-'*30, 'SIMILARITY_MATRIX', '-'*30, '\n')
        print(similarity_df.head())
        print(similarity_df.shape)
    else:
        similarity_df = load('SIMILARITY_MATRIX.pkl')


    if 'RECALL.pkl' not in os.listdir():
        recall = get_recall(similarity_df)
        dump(recall, 'RECALL.pkl')
    else:
        recall = load('RECALL.pkl')

    print()
    print('*'*150)
    print()
    print('AVERAGE RECALL: ', sum(recall)/len(recall))
    print()
    print('*'*150)
    print()

#!/usr/bin/env python3

from joblib import dump
import os
import cv2
from collections import defaultdict
import pandas as pd
import numpy as np


def get_luv(img):
    r, g, b = [], [], []
    for i in range(img.shape[0]):
        r.append(img[i, :, 2].tolist())
        g.append(img[i, :, 1].tolist())
        b.append(img[i, :, 0].tolist())

    l, u, v = [], [], []
    for i in range(len(r)):
        temp_l, temp_u, temp_v = [], [], []
        for j in range(len(r[i])):
            temp_l.append(r[i][j]+g[i][j]+b[i][j])
            temp_u.append(-2*r[i][j] + g[i][j] + b[i][j] + (255*2))
            temp_v.append(-g[i][j] + b[i][j] + 255)
        l.append(temp_l)
        u.append(temp_u)
        v.append(temp_v)

    #print(img.shape)
    #print(len(l))
    #print(len(l[0]))
    
    return l, u, v


if __name__ == '__main__':

    IMG_FOLDER = '/mnt/disks/disk_1/be-project/dataset/test1-renamed'
    files = sorted(os.listdir(IMG_FOLDER))

    luv_img = defaultdict(list)

    if 'kluv-matrixed.pkl' not in os.listdir() or True:
        for f in files:
            if '.jpg' in f:
                l, u, v = get_luv(cv2.imread(os.path.join(IMG_FOLDER, f)))
                index = f.split('.')[0]
                luv_img[index].append(l)
                luv_img[index].append(u)
                luv_img[index].append(v)
                print(f'Image {index} done')

        df = pd.DataFrame.from_dict(luv_img, orient='index')
        dump(df, 'kluv-matrixed.pkl')
        
        '''
        print(len(df.iloc[0, 0]))
        print(len(df.iloc[:, 0][0][0]))
        print(df.iloc[:, 1])
        print(df.iloc[:, 2])
        print(df.shape)
        '''

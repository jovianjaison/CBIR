#!/usr/bin/env python3

from joblib import dump
import os
import cv2
from collections import defaultdict
import pandas as pd
import numpy as np


def get_luv(img):
    img = np.array([[[100, 100, 200], [0, 0, 0]]*(img.shape[1]//2)]*img.shape[0])
    print(img)
    print(img.shape)
    r, g, b = [], [], []
    for i in range(img.shape[0]):
        r.extend(img[i, :, 2].tolist())
        g.extend(img[i, :, 1].tolist())
        b.extend(img[i, :, 0].tolist())

    l, u, v = [], [], []
    for i in range(len(r)):
        l.append(r[i]+g[i]+b[i])
        u.append(-2*r[i] + g[i] + b[i] + (255*2))
        v.append(-g[i] + b[i] + 255)

    return l, u, v


if __name__ == '__main__':

    IMG_FOLDER = '/mnt/disks/disk_1/be-project/dataset/test1-renamed'
    files = sorted(os.listdir(IMG_FOLDER))
    #images = [ (int(f.split('.')[0]), cv2.imread(os.path.join(IMG_FOLDER, f))) for f in files if '.jpg' in f]

    luv_img = defaultdict(list)

    if 'kluv.pkl' not in os.listdir() or True:
        for f in files:
            if '.jpg' in f:
                l, u, v = get_luv(cv2.imread(os.path.join(IMG_FOLDER, f)))
                index = f.split('.')[0]
                luv_img[index].append(l)
                luv_img[index].append(u)
                luv_img[index].append(v)
                break

        df = pd.DataFrame.from_dict(luv_img, orient='index')
        #dump(df, 'kluv.pkl')

        print(df.iloc[:, 0])
        print(df.iloc[:, 1])
        print(df.iloc[:, 2])
        print(df.shape)


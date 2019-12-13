#!/usr/bin/env python3

from joblib import dump
import os
import cv2
from collections import defaultdict
import pandas as pd
from skimage import feature
import numpy as np


def get_lbp(img):
    temp = []
    for i in (0, 1, 2):
        temp.append(feature.local_binary_pattern(img[:, :, i], 8, 1, 'default'))
    temp = np.array(temp)
    return temp

def get_rgb(img):
    r, g, b = [], [], []
    lbp_img = get_lbp(img)
    for i in range(lbp_img.shape[1]):
        r.extend(lbp_img[2, i, :].tolist())
        g.extend(lbp_img[1, i, :].tolist())
        b.extend(lbp_img[0, i, :].tolist())

    return r, g, b


if __name__ == '__main__':

    IMG_FOLDER = '/mnt/disks/disk_1/be-project/dataset/test1-renamed'
    #IMG_FOLDER = '/home/rohan/Personal/College-work/BE Proj/BEProject/dataset/test1-renamed'
    files = sorted(os.listdir(IMG_FOLDER))

    rgb_img = defaultdict(list)

    if 'rgb_lbp.pkl' not in os.listdir():
        for f in files:
            if '.jpg' in f:
                r, g, b = get_rgb(cv2.imread(os.path.join(IMG_FOLDER, f)))
                index = f.split('.')[0]
                rgb_img[index].append(r)
                rgb_img[index].append(g)
                rgb_img[index].append(b)
                print(f'IMG {index} done')
        df = pd.DataFrame.from_dict(rgb_img, orient='index')
        dump(df, 'rgb_lbp.pkl')

        print(df.head())
        print(df.shape)


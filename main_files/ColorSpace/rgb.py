#!/usr/bin/env python3

from joblib import dump
import os
import cv2
from collections import defaultdict
import pandas as pd


def get_rgb(img):
    r, g, b = [], [], []
    for i in range(img.shape[0]):
        r.extend(img[i, :, 2].tolist())
        g.extend(img[i, :, 1].tolist())
        b.extend(img[i, :, 0].tolist())

    return r, g, b


if __name__ == '__main__':

    IMG_FOLDER = '/mnt/disks/disk_1/be-project/dataset/test1-renamed'
    files = sorted(os.listdir(IMG_FOLDER))

    rgb_img = defaultdict(list)

    if 'rgb.pkl' not in os.listdir():
        for f in files:
            if '.jpg' in f:
                r, g, b = get_rgb(cv2.imread(os.path.join(IMG_FOLDER, f)))
                index = f.split('.')[0]
                rgb_img[index].append(r)
                rgb_img[index].append(g)
                rgb_img[index].append(b)

        df = pd.DataFrame.from_dict(rgb_img, orient='index')
        dump(df, 'rgb.pkl')

        print(df.head())
        print(df.shape)


#!/usr/bin/env python3

from joblib import dump
import os
import cv2
from collections import defaultdict
import pandas as pd


def get_ycbcr(img):
    r, g, b = [], [], []
    for i in range(img.shape[0]):
        r.extend(img[i, :, 2].tolist())
        g.extend(img[i, :, 1].tolist())
        b.extend(img[i, :, 0].tolist())

    y, cb, cr = [], [], []
    for i in range(len(r)):
        y.append((0.2989 * r[i]) + (0.5866 * g[i]) + (0.1145 * b[i]))
        cb.append((-0.1688 * r[i]) + (-0.3312 * g[i]) + (0.5 * b[i]) + 127.5)
        cr.append((0.5 * r[i]) + (-0.4184 * g[i]) + (-.0816 * b[i]) + 127.5)

    return y, cb, cr


if __name__ == '__main__':

    IMG_FOLDER = '/mnt/disks/disk_1/be-project/dataset/test1-renamed'
    files = sorted(os.listdir(IMG_FOLDER))

    ycbcr_img = defaultdict(list)
    if 'ycbcr.pkl' not in os.listdir():
        for f in files:
            if '.jpg' in f:
                y, cb, cr = get_ycbcr(cv2.imread(os.path.join(IMG_FOLDER, f)))
                index = f.split('.')[0]
                ycbcr_img[index].append(y)
                ycbcr_img[index].append(cb)
                ycbcr_img[index].append(cr)

        df = pd.DataFrame.from_dict(ycbcr_img, orient='index')
        dump(df, 'ycbcr.pkl')
        
        print(df.head())
        print(df.shape)


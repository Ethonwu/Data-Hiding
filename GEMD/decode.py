#!/usr/bin/env python
import math
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
img_w , img_l = img.shape
allpixel=img_l*img_w
pixel_array = np.empty(allpixel)
n = 2
secret_len = 6
index = 0
for i in range(0,img_w):
    for j in range(0,img_l):
        pixel_array[index] = img[i,j]
        index =index + 1
f =0
flag = 0
modnum = pow(2,n+1)
if secret_len%n != 0:
    th = secret_len/n + 1
else:
    th = secret_len / n
for i in range(0,secret_len,n+1):
    GEMD = 0.0
    for j in range(0,n+1):
        GEMD = GEMD + pixel_array[f+j-1]*(pow(2,j)-1)
    f = f + n
    print GEMD%(modnum)

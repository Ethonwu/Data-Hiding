#!/usr/bin/env python
import math
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
#np.set_printoptions(threshold=np.nan) #See all array value
secret = "101101"
n = 2
img = cv2.imread('Lena.bmp', cv2.IMREAD_GRAYSCALE)

img_w , img_l = img.shape  # Get the w and l
stego_img = img # Creat array for new pic
#secret_binary = ''.join(format(ord(x), 'b') for x in secret) # Secret to binary
secret_binary = secret
#print "SecretBinary:",secret_binary

modmath = pow(2,n+1)
secret_len = len(secret_binary)
arrayori = np.empty(img_l*img_w+n) #Orgin array from img
arrayste = np.empty(img_l*img_w+n) #Steg  array from final img

index =0
for i in range(0,img_w):
    for j in range(0,img_l):
        arrayori[index] = img[i,j]
        if arrayori[i] == 255:
            arrayste[i] = arrayste[i] - 1
        if arrayori[i] == 0:
            arrayste[i] = arrayste[i] + 1
        index = index + 1

##GEMD Part
index = 0
for i in range(0,secret_len,n+1):
    GEMD = 0.0
    eachsecret = ""
    deeachsecret = 0.0
    d = 0.0
    eachsecret = secret[i:i+n+1]
    for j in range(0,n):
        GEMD = GEMD + arrayori[index+j]*(pow(2,j+1)-1)
    deeachsecret = float(int(eachsecret,2))
    d = (deeachsecret - (GEMD%modmath))%modmath
    print d
    if d < 0:
        d = d + modmath
    if d <= pow(2,n) and d >= 0:
        if d == pow(2,n):
            flag = n - 1
            for j in range(0,n):
                arrayste[flag+index] = arrayori[flag+index]
                flag = flag - 1
        else:
            strford = "{0:b}".format(int(d))
            for j in range(0,n):
                if len(strford) < n+1:
                    strford = "0" + strford 
            print strford
            flag = n - 1
            for j in range(0,n):
                if strford[j] == strford[j+1]:
                    arrayste[flag+index] = arrayori[flag+index]
                if strford[j] == '0' and strford[j+1] == '1':
                    arrayste[flag+index] = arrayori[flag+index]+1
                if strford[j] == '1' and strford[j+1] == '0':
                    arrayste[flag+index] = arrayori[flag+index]-1
                flag = flag -1
    if d > pow(2,n):
        d = modmath - d
        strford = str("{0:b}".format(int(d)))
        for j in range(0,n):
            if len(strford) < n+1:
                strford = "0" + strford 
        flag = n - 1
        for j in range(0,n):
            if strford[j] == strford[j+1]:
                arrayste[flag+index] = arrayori[flag+index]
            if strford[j] == '0' and strford[j+1] == '1':
                arrayste[flag+index] = arrayori[flag+index]-1
            if strford[j] == '1' and strford[j+1] == '0':
                arrayste[flag+index] = arrayori[flag+index]+1
            flag = flag - 1


    index = index + n
### 
#print arrayori[0:10]
#print arrayste[0:10]
### Print img
stegnum = 0;
secret_all = secret_len / n
for i in range(0,img_w):
    for j in range(0,img_l):
        if stegnum < secret_all or stegnum == secret_all-1:
            stego_img[i,j] = int(arrayste[stegnum]) 
        if stegnum > secret_all:
            arrayste[stegnum] = arrayori[stegnum]
            stego_img[i,j] = arrayori[stegnum]
        stegnum = stegnum + 1

cv2.imwrite('output.png', stego_img)
print arrayori[0:10]
print arrayste[0:10]
#print img[6,6]
#plt.figure("Picture") 
#plt.imshow(img,cmap="gray")
#plt.show()

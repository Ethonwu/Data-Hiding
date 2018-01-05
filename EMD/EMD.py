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

modmath = 2*n + 1
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

##EMD Part
secret_len = secret_len - 1
for i in range(0,secret_len,n):
    EMD = float()
    eachsecret = float()
    d = float()
    #eachsecret = 0.0 
    eachsecret = ""
    desecret=0.0
    EMD = 0.0
    d = 0.0
    b = n
    for j in range(0,n):
        #eachsecret = eachsecret + (int(secret_binary[i+j])*pow(2,b-1))
        eachsecret = eachsecret + str(secret_binary[i+j])
        #print int(secret_binary[i+j])
        #print "EachSecret:",eachsecret
        EMD = EMD + arrayori[i+j]*(1+j)
        b = b - 1
    desecret = float(int(eachsecret,2))
    print desecret
    #d = (eachsecret-(EMD%modmath))%modmath
    d = (desecret-(EMD%modmath))%modmath
    print d
    if d < 0:
        d = d + modmath
    if d == 0:
        for k in range(0,n):
            arrayste[i+k] = arrayori[i+k]
    if d < math.floor(float(modmath)/2):
        for k in range(0,n):
            arrayste[i+k] = arrayori[i+k]
            if k == d-1:
                arrayste[i+k] = arrayori[i+k] + 1
    else:
        d = modmath - d
        for k in range(0,n):
            arrayste[i+k] = arrayori[i+k]
            if k == d-1:
                #arrayste[i+k] = arrayori[i+k] + 1
                arrayste[i+k] = arrayori[i+k] - 1
### 
### Print img
stegnum = 0;
for i in range(0,img_w):
    for j in range(0,img_l):
        if stegnum < secret_len or stegnum == secret_len:
            stego_img[i,j] = int(arrayste[stegnum]) 
        if stegnum > secret_len:
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

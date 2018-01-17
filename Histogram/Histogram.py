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
stego_img_w , stego_img_l = img_w , img_l
print stego_img_l,stego_img_w
#secret_binary = ''.join(format(ord(x), 'b') for x in secret) # Secret to binary
secret_binary = secret
#print "SecretBinary:",secret_binary

blocksize = 4



#cv2.imwrite('output.png', stego_img)
#print img[6,6]
#plt.figure("Picture") 
#plt.imshow(img,cmap="gray")
#plt.show()

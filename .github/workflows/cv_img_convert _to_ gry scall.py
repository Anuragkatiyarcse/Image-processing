"""import cv2
img = cv2.imread("D:\kajal.png")
cv2.imshow('output Image', img)
cv2.waitKey(0)

#method 1st
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image scale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()"""

"""import cv2
img = cv2.imread("D:\kajal.png",0)
cv2.imshow('gray scale image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

import cv2
"""
img = cv2.imread("D:\kajal.png")

img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image',img_HSV)

cv2.imshow('Hue channel', img_HSV[:,:,0])
cv2.imshow('Saturation', img_HSV[:,:,1])
cv2.imshow('abc', img_HSV[:,:,2])


cv2.waitKey(0)
cv2.destroyAllWindows()"""

import numpy as np
"""
img = cv2.imread("D:\kajal.png")
cv2.imshow("original",img)
cv2.waitKey(0)

B,G,R = cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)

cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)

cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()"""

"""
img = cv2.imread("D:\kajal.png")

H,W = img.shape[:2]
Rot_Mtx = cv2.getRotationMatrix2D((W/4,H/4),60, .5)
Rot_image = cv2.warpAffine(img,Rot_Mtx,(W,H))

cv2.imshow('Rotaded Image', Rot_image)

cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""
import cv2
img = cv2.imread("D:\kajal.png")

rot_img = cv2.transpose(img)
cv2.imshow('rotated Image', rot_img)
cv2.imshow('original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""
img = cv2.imread("D:\kajal.png")

img_scaled = cv2.resize(img, None, fx =0.75, fy = 0.50)

cv2.imshow('resize Image', img_scaled)

cv2.imshow('original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""
img = cv2.imread("D:\kajal.png")

S = cv2.pyrDown(img)
L = cv2.pyrUp(img)

cv2.imshow('Large Image', L)
cv2.imshow('smaler Image', S)
cv2.imshow('original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
img = cv2.imread("D:\kajal.png")

H, W = img.shape[:2]
start_row, start_col = int(H*.25), int(W*.25)

end_row, end_col = int(H*.75), int(W*.75)

cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('original Image', img)
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
# image  Arithmaatice
img = cv2.imread("D:\kajal.png")

cv2.imshow('original Image', img)
M = np.ones(img.shape, dtype="uint8")*150

added = cv2.add(img,M)
sub = cv2.subtract(img,M)
mul = cv2.multiply(img,M)

cv2.imshow("Added",added)
cv2.imshow("Subtract", sub)
cv2.imshow("multiply",mul)

cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""
#Bitwise operation

square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255, -1)
cv2.imshow("Square", square)

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Ellipse", ellipse)

And = cv2.bitwise_and(square,ellipse)
cv2.imshow("And",And)

Or = cv2.bitwise_or(square,ellipse)
cv2.imshow("Or",Or)

Xor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor",Xor)

Not = cv2.bitwise_not(square,ellipse)
cv2.imshow("Not",Not)

cv2.waitKey(0)
cv2.destroyAllWindows()"""


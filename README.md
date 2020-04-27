# Image-processing
import cv2
img = cv2.imread("D:\kajal.png")
cv2.imshow('output Image', img)
cv2.waitKey(0)

#method 1st
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image scale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

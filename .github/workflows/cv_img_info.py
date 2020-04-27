import cv2
img = cv2.imread("D:\kajal.png")
cv2.imshow('output Image', img)

print(img.shape)

print("hight pixel : ",img.shape[0])
print("hight pixel : ",img.shape[1])

cv2.waitKey(0)
cv2.destroyAllWindows()





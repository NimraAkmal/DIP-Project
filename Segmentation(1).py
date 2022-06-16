import numpy as np
import cv2 as cv

gray_img = cv.imread('pic1.jpg',0)


def get_binary_img(img):
 bin_img = np.zeros(shape=(img.shape), dtype=np.uint8)
 h = img.shape[0]
 w = img.shape[1]
 for i in range(h):
    for j in range(w):
        if img[i][j] > 140:
            bin_img[i][j] = 255
        else:
            bin_img[i][j] = 0
 return bin_img
# call
bin_img = get_binary_img(gray_img)
cv.imwrite('bin_img.jpg',bin_img)
# cv.imshow('SHOW',bin_img)

#resizing
width = 450
height = 450
dim = (width, height)
# resize image
orig= cv.resize(bin_img, dim, interpolation=cv.INTER_AREA)
cv.imshow('resized', orig)
cv.waitKey(0)
#now adjusting
dim = np.shape(orig)
rows = dim[0]
cols = dim[1]
print(rows,cols)
for i in range(rows):
    for j in range(0,35):
        orig[i][j]=255
for i in range(rows):
    for j in range(cols-35,cols):
        orig[i][j]=255
for i in range(0,28):
    for j in range(cols):
        orig[i][j]=255
for i in range(140):
    for j in range(150-i):
        orig[i][j]=255

cv.imshow('show',orig)

#errosion
kernel = np.ones((7,7), np.uint8)
img_err= cv.dilate(orig, kernel, iterations=1)
cv.imshow('Input', orig)
cv.imshow('Err', img_err)
#dialation
kernel1 = np.ones((13,13), np.uint8)
img_dil = cv.erode(img_err, kernel1, iterations=1)
print(img_dil.shape)
cv.imwrite('Lung_Dialated.jpg',img_dil)
cv.imshow('Dial', img_dil)
cv.waitKey(0)


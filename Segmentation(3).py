import numpy as np
import cv2 as cv

orignal=cv.imread('pic1.jpg',0)
Mask_app=cv.imread('Segmented Image.jpg',0)
rows=Mask_app.shape[0]
cols=Mask_app.shape[1]
for i in range(rows):
    for j in range(cols):
        if Mask_app[i][j]==0:
            Mask_app[i][j]=255
        else:
            Mask_app[i][j] = 0


width = 450
height = 450
dim = (width, height)

# resize image
orig= cv.resize(orignal, dim, interpolation=cv.INTER_AREA)
cv.imshow('orig', orig)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv.filter2D(src=orig, ddepth=-1, kernel=kernel)
cv.imshow('orig_sharp', image_sharp)


Mask=cv.bitwise_and(orig,Mask_app)
cv.imshow('mask', Mask)
cv.waitKey(0)
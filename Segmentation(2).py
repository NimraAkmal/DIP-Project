import numpy as np
import cv2 as cv
img = cv.imread("Lung_Dialated.jpg", cv.IMREAD_GRAYSCALE)
rows, cols = img.shape
k1 = np.mean(img) - 30
k2 = np.mean(img) + 30
c1 = []
c2 = []
mean_thresh_img = np.copy(img)
segmented_img = np.copy(img)
while True:
 for r in range(0, rows):
    for c in range(0, cols):
        pixel = img[r, c]
        d1 = np.sqrt(np.sum(np.square(pixel - k1)))
        d2 = np.sqrt(np.sum(np.square(pixel - k2)))
        min_val = min(d1, d2)
        if min_val == d1:
            c1.append(pixel)
        elif min_val == d2:
            c2.append(pixel)
 m1 = np.mean(c1)
 m2 = np.mean(c2)
 if m1 == k1 and m2 == k2:
  break
 else:
  k1 = m1
  k2 = m2
  c1 = []
  c2 = []
for i in range(0, len(c1)):
    mean_thresh_img[mean_thresh_img == c1[i]] = m1
for i in range(0, len(c2)):
    mean_thresh_img[mean_thresh_img == c2[i]] = m2
for i in range(0, len(c1)):
    segmented_img[segmented_img == c1[i]] = 0
for i in range(0, len(c2)):
    segmented_img[segmented_img == c2[i]] = 255
# cv.imshow("Mean Thresholded Image", mean_thresh_img)
cv.imshow("Segmented Image", segmented_img)
cv.imwrite('Segmented Image.jpg',segmented_img)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

img = cv.imread('images/taylor.jpg')
# cv.flip(img, flipCode) # flipCode 三种取值: 0，正数，负数
dst_1 = cv.flip(img, 0)
dst_2 = cv.flip(img, 1)
dst_3 = cv.flip(img, -1)

cv.imshow('img', img)
cv.imshow('dst_1', dst_1)
cv.imshow('dst_2', dst_2)
cv.imshow('dst_3', dst_3)

cv.waitKey(0)
cv.destroyAllWindows()
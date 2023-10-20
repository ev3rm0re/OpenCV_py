import numpy as np
import cv2 as cv

img = cv.imread('images/taylor.jpg')
cv.imshow('img', img)
img_h = np.hstack((img, img))
img_v = np.vstack((img, img))

cv.imshow('img_h', img_h)
cv.imshow('img_v', img_v)

cv.waitKey(0)
cv.destroyAllWindows()
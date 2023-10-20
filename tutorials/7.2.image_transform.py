import numpy as np
import cv2 as cv

img = cv.imread('roi.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img', img)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
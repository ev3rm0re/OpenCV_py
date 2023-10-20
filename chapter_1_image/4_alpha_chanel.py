import numpy as np
import cv2 as cv

bgr_img = cv.imread('images/roi.jpg')
bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGBA)
cv.imshow('BGRA', bgra_img)
b, g, r, a = cv.split(bgra_img)
a[:,:] = 172
bgra_172 = cv.merge([b, g, r, a])
a[:,:] = 0
bgra_0 = cv.merge([b, g, r, a])
cv.imshow('A = 172', bgra_172)
cv.imshow('A = 0', bgra_0)
cv.imwrite('images/bgra_img.png', bgra_img)
cv.imwrite('images/bgra_172.png', bgra_172)
cv.imwrite('images/bgra_0.png', bgra_0)

cv.waitKey(0)
cv.destroyAllWindows()
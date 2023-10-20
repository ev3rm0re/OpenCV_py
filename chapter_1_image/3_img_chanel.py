import numpy as np
import cv2 as cv

img = cv.imread('images/roi.jpg')
cv.imshow('img', img)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv_img)
h, s, v = cv.split(hsv_img)
s[:,:] = 255
cv.imshow('h', h)
cv.imshow('s', s)
cv.imshow('v', v)
hsv_img = cv.merge([h, s, v])
new_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
cv.imshow('new_img', new_img)

cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
import cv2 as cv

img = cv.imread('images/taylor.jpg')
dst_1 = cv.resize(img, (200, 300)) # 按dsize缩放
dst_2 = cv.resize(img, None, fx=0.3, fy=0.3) # 使用fx参数和fy参数控制缩放时，dsize参数值必须使用None，否则fx和fy失效

cv.imshow('origin_img', img)
cv.imshow('dst_1', dst_1)
cv.imshow('dst_2', dst_2)

cv.waitKey(0)
cv.destroyAllWindows()
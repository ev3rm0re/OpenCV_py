import numpy as np
import cv2 as cv

# 阈值处理
# retval, dst = cv2.threshold(src, thresh, maxval, type)
# src：被处理的图像，可以是多通道图像
# thresh：阈值，阈值在125～150取值的效果最好
# maxval：阈值处理采用的最大值
# type：阈值处理类型
## 返回值：
# retval：处理时采用的阈值
# dst：经过阈值处理后的图像

img = cv.imread('images/black.jpg', 0)
t1, dst1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # 图像中凡是大于127的像素值都变成了255（纯白色），小于或等于127的像素值都变成了0（纯黑色）
t2, dst2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # 反二值化处理
t3, dst3 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # 低于阈值零处理
t4, dst4 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # 截断阈值处理
cv.imshow('img', img)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.imshow('dst3', dst3)
cv.imshow('dst4', dst4)

cv.waitKey(0)
cv.destroyAllWindows()
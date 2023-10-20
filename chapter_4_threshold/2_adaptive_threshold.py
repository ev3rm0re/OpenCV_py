import numpy as np
import cv2 as cv

# 自适应阈值处理
# dst = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# src：被处理的图像。需要注意的是，该图像需是灰度图像
# maxValue：阈值处理采用的最大值
# adaptiveMethod：自适应阈值的计算方法
# thresholdType：阈值处理类型；需要注意的是，阈值处理类型需是cv2.THRESH_BINARY或cv2.THRESH_BINARY_INV中的一个
# blockSize：一个正方形区域的大小。例如，5指的是5×5的区域
# C：常量。阈值等于均值或者加权值减去这个常量
## 返回值
# dst：经过阈值处理后的图像

img = cv.imread('images/taylorswift.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 转化为灰度图像
img_mean = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3) # 计算方法为cv.ADAPTIVE_THRESH_MEAN_C
img_gauss = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 3) # 计算方法为cv.ADAPTIVE_THRESH_GAUSSIAN_C

cv.imshow('img_gray', img_gray)
cv.imshow('img_mean', img_mean)
cv.imshow('img_gauss', img_gauss)

cv.waitKey(0)
cv.destroyAllWindows()
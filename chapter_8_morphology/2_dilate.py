import cv2 as cv
import numpy as np

# dst = cv2.dilate(src, kernel, anchor, iterations, borderType, borderValue)
# src：原始图像
# kernel：膨胀使用的核
# anchor：可选参数，核的锚点位置
# iterations：可选参数，操作的迭代次数，默认值为1
# borderType：可选参数，边界样式，建议默认
# borderValue：可选参数，边界值，建议默认
# 返回值
# dst：经过膨胀之后的图像

img = cv.imread('images/taylorswift.jpg')
k = np.ones((9, 9), np.uint8)
cv.imshow('img', img)
dst = cv.dilate(img, k)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
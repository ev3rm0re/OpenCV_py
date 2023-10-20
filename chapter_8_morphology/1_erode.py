import cv2 as cv
import numpy as np

# dst = cv2.erode(src, kernel, anchor, iterations, borderType, borderValue)
# src：原始图像
# kernel：腐蚀使用的核
# anchor：可选参数，核的锚点位置
# iterations：可选参数，腐蚀操作的迭代次数，默认值为1
# borderType：可选参数，边界样式，建议默认
# borderValue：可选参数，边界值，建议默认
# 返回值
# dst：经过腐蚀之后的图像

img = cv.imread('images/taylorswift.jpg')
k = np.ones((3, 3), np.uint8)
cv.imshow('img', img)
dst = cv.erode(img, k)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
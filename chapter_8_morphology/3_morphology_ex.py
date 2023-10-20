import cv2 as cv
import numpy as np

# dst = cv2.morphologyEx(src, op, kernel, anchor, iterations, borderType, borderValue)
# src：原始图像
# op：操作类型
# kernel：操作过程中使用的核
# anchor：可选参数，核的锚点位置
# iterations：可选参数，迭代次数，默认值为1
# borderType：可选参数，边界样式，建议默认
# borderValue：可选参数，边界值，建议默认
# 返回值
# dst：操作之后得到的图像

img = cv.imread('images/taylorswift.jpg')
k = np.ones((5, 5), np.uint8)
cv.imshow('img', img)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, k) # 梯度运算：膨胀图减腐蚀图
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, k) # 顶帽运算，原图减开运算图 # 开运算：先腐蚀后膨胀
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, k) # 黑帽运算，闭运算图减原图 # 闭运算：先膨胀后腐蚀
cv.imshow('gradient', gradient)
cv.imshow('tophat', tophat)
cv.imshow('blackhat', blackhat)

cv.waitKey(0)
cv.destroyAllWindows()
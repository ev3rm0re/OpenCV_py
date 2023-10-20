import numpy as np
import cv2 as cv
################################################################
# dst = cv2.warpAffine(src, M, dsize, flags, borderMode, borderValue)
# M：一个2行3列的矩阵，根据此矩阵的值变换原图中的像素位置，M矩阵中的数字采用32位浮点格式
# * M = [[a, b, c],[d, e, f]]
# * 新x = 原x × a + 原y × b + c
# * 新y = 原x × d + 原y × e + f
################################################################
# dsize：输出图像的尺寸大小
# flags：可选参数，插值方式，建议使用默认值
# borderMode：可选参数，边界类型，建议使用默认值
# borderValue：可选参数，边界值，默认为0，建议使用默认值
# dst：经过反射变换后输出图像
################################################################
## 平移：M = [[1, 0, 水平移动的距离],[0, 1, 垂直移动的距离]]
################################################################
## 旋转：M = cv2.getRotationMatrix2D(center, angle, scale)
### center：旋转的中心点坐标。
### angle：旋转的角度（不是弧度）。正数表示逆时针旋转，负数表示顺时针旋转。
### scale：缩放比例，浮点类型。如果取值1，表示图像保持原来的比例。
################################################################
img = cv.imread('images/taylor.jpg')
rows = len(img)
cols = len(img[0])
center = (rows / 2, cols / 2)
M = cv.getRotationMatrix2D(center, 30, 0.8)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', img)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
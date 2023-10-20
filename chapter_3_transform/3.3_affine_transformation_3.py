import numpy as np
import cv2 as cv
##################################################################
# 透视
# dst = cv2.warpPerspective(src, M, dsize, flags, borderMode, borderValue)
# src：原始图像
# M：一个3行3列的矩阵，根据此矩阵的值变换原图中的像素位置
## M = cv2.getPerspectiveTransform(src, dst)
## * src：原图4个点坐标，格式为4行2列的32位浮点数列表，例如：[[0, 0], [1, 0], [0, 1],[1, 1]]
## * dst：透视图的4个点坐标，格式与src一样
## * M：getPerspectiveTransform()方法计算出的仿射矩阵
# dsize：输出图像的尺寸大小
# flags：可选参数，插值方式，建议使用默认值
# borderMode：可选参数，边界类型，建议使用默认值
# borderValue：可选参数，边界值，默认为0，建议使用默认值
# dst：经过透视变换后输出图像

img = cv.imread('images/taylor.jpg')
rows = len(img)
cols = len(img[0])
# 原图四个点
p1 = np.zeros((4, 2), np.float32)
p1[0] = [0, 0]
p1[1] = [cols - 1, 0]
p1[2] = [0, rows - 1]
p1[3] = [cols - 1, rows - 1]
# 透视图四个点
p2 = np.zeros((4, 2), np.float32)
p2[0] = [100, 0]
p2[1] = [cols - 100, 0]
p2[2] = [0, rows - 1]
p2[3] = [cols - 1, rows - 1]

M = cv.getPerspectiveTransform(p1, p2)
dst = cv.warpPerspective(img, M, (cols, rows))

cv.imshow('img', img)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
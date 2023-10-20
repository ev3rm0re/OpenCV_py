import numpy as np
import cv2 as cv
############################################################
# 倾斜
# M = cv2.getAffineTransform(src, dst)
# src：原图3个点坐标，格式为3行2列的32位浮点数列表，例如：[[0, 1], [1, 0], [1, 1]]
# dst：倾斜图像的3个点坐标，格式与src一样
# M：getAffineTransform()方法计算出的仿射矩阵
############################################################

img = cv.imread('images/taylor.jpg')
rows = len(img)
cols = len(img[0])
# 原图三个点
p1 = np.zeros((3, 2), np.float32)
p1[0] = [0, 0]
p1[1] = [cols - 1, 0]
p1[2] = [0, rows - 1]
# 倾斜图三个点
p2 = np.zeros((3, 2), np.float32)
p2[0] = [50, 0]
p2[1] = [cols - 1, 0]
p2[2] = [0, rows - 1]
M = cv.getAffineTransform(p1, p2)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', img)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()
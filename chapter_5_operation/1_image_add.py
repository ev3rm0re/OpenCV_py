import numpy as np
import cv2 as cv

# 图像的加法
# dst = cv2.add(src1, src2, mask, dtype)
# src1：第一幅图像
# src2：第二幅图像
# mask：可选参数，掩模，建议使用默认值
# dtype：可选参数，图像深度，建议使用默认值
## 返回值
# dst：相加之后的图像。如果相加之后值的结果大于255，则取255

img1 = np.zeros((300, 300, 3), np.uint8)
img2 = np.zeros((300, 300, 3), np.uint8)
img3 = np.zeros((300, 300, 3), np.uint8)
img1[:,:,0] = 255
img2[:,:,1] = 255
img3[:,:,2] = 255
cv.imshow('1', img1)
cv.imshow('2', img2)
cv.imshow('3', img3)
img = cv.add(img1, img2)
cv.imshow('1 + 2', img)
img = cv.add(img, img3)
cv.imshow('1 + 2 + 3', img)

cv.waitKey(0)
cv.destroyAllWindows()
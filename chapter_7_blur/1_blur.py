import cv2 as cv

# dst = cv2.blur(src, ksize, anchor, borderType)
# src：被处理的图像
# ksize：滤波核大小，其格式为(高度，宽度)，建议使用如(3, 3)、(5, 5)、(7, 7)等宽、高相等的奇数边长。滤波核越大，处理之后的图像就越模糊
# anchor：可选参数，滤波核的锚点，建议采用默认值，可以自动计算锚点
# borderType：可选参数，边界样式，建议采用默认值
# 返回值
# dst：经过均值滤波处理之后的图像

img = cv.imread('images/taylorswift.jpg')
dst1 = cv.blur(img, (3, 3))
dst2 = cv.blur(img, (5, 5))
dst3 = cv.blur(img, (9, 9))

cv.imshow('img', img)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.imshow('dst3', dst3)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

# dst = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
# src：被处理的图像
# ksize：滤波核的大小，宽高必须是奇数，如(3, 3)、(5, 5)等
# sigmaX：卷积核水平方向的标准差
# sigmaY：卷积核垂直方向的标准差
# 修改sigmaX或sigmaY的值都可以改变卷积核中的权重比例。如果不知道如何设计这2个参数值，就直接把这2个参数的值写成0，该方法就会根据滤波核的大小自动计算合适的权重比例
# borderType：可选参数，边界样式，建议使用默认值
# 返回值
# dst：经过高斯滤波处理之后的图像

img = cv.imread('images/taylorswift.jpg')
dst1 = cv.GaussianBlur(img, (5, 5), sigmaX=0, sigmaY=0)
dst2 = cv.GaussianBlur(img, (9, 9), sigmaX=0, sigmaY=0)
dst3 = cv.GaussianBlur(img, (15, 15), sigmaX=0, sigmaY=0)

cv.imshow('img', img)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.imshow('dst3', dst3)

cv.waitKey(0)
cv.destroyAllWindows()
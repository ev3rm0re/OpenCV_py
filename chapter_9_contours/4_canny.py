import cv2 as cv

# edges = cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)
# image：检测的原始图像
# threshold1：计算过程中使用的第一个阈值，可以是最小阈值，也可以是最大阈值，通常用来设置最小阈值
# threshold2：计算过程中使用的第二个阈值，通常用来设置最大阈值
# apertureSize：可选参数，Sobel算子的孔径大小
# L2gradient：可选参数，计算图像梯度的标识，默认值为False。值为True时采用更精准的算法进行计算
# 返回值
# edges：计算后得出的边缘图像，是一个二值灰度图像

img = cv.imread('images/template.jpg')
r1 = cv.Canny(img, 10, 50)
r2 = cv.Canny(img, 100, 200)
r3 = cv.Canny(img, 400, 600)

cv.imshow('img', img)
cv.imshow('r1', r1)
cv.imshow('r2', r2)
cv.imshow('r3', r3)

cv.waitKey(0)
cv.destroyAllWindows()
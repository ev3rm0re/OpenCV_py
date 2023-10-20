import cv2 as cv

# dst = cv2.medianBlur(src, ksize)
# src：被处理的图像
# ksize：滤波核的边长，必须是大于1的奇数，如3、5、7等。该方法根据此边长自动创建一个正方形的滤波核
# dst：经过中值滤波处理之后的图像

img = cv.imread('images/taylorswift.jpg')
dst1 = cv.medianBlur(img, 3)
dst2 = cv.medianBlur(img, 5)
dst3 = cv.medianBlur(img, 9)

cv.imshow('img', img)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.imshow('dst3', dst3)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

# src：被处理的图像
# d：以当前像素为中心的整个滤波区域的直径。如果d<0，则自动根据sigmaSpace参数计算得到。该值与保留的边缘信息数量成正比，与方法运行效率成反比
# sigmaColor：参与计算的颜色范围，这个值是像素颜色值与周围颜色值的最大差值，只有颜色值之差小于这个值时，周围的像素才进行滤波计算。值为255时，表示所有颜色都参与计算
# sigmaSpace：坐标空间的σ（sigma）值，该值越大，参与计算的像素数量就越多
# borderType：可选参数，边界样式，建议默认
# 返回值
# dst：经过双边滤波处理之后的图像

img = cv.imread('images/taylorswift.jpg')
dst1 = cv.GaussianBlur(img, (15, 15), sigmaX=0, sigmaY=0) # 使用大小为15*15的滤波核进行高斯滤波
dst2 = cv.bilateralFilter(img, 15, 120, 100) # 双边滤波，选取范围直径为15，颜色差为120
# 高斯滤波模糊了整个画面，但双边滤波保留了较清晰的边缘信息
cv.imshow('img', img)
cv.imshow('Gauss', dst1)
cv.imshow('bilateral', dst2)

cv.waitKey(0)
cv.destroyAllWindows()
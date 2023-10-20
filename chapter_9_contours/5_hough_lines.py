import cv2 as cv
import numpy as np

# lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap)
# image：检测的原始图像
# rho：检测直线使用的半径步长，值为1时，表示检测所有可能的半径步长
# theta：搜索直线的角度，值为π/180°时，表示检测所有角度
# threshold：阈值，该值越小，检测出的直线就越多
# minLineLength：线段的最小长度，小于该长度的线段不记录到结果中
# maxLineGap：线段之间的最小距离
# 返回值
# lines：一个数组，元素为所有检测出的线段，每条线段是一个数组，代表线段两个端点的横、纵坐标，格式为[[[x1, y1, x2, y2], [x1, y1, x2, y2]]]


img = cv.imread('images/pen.jpg')
o = img.copy()
o = cv.medianBlur(o, 5)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
binary = cv.Canny(o, 50, 150)
lines = cv.HoughLinesP(binary, 1, np.pi / 180, 15, minLineLength=100, maxLineGap=18)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow('canny', binary)
cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()
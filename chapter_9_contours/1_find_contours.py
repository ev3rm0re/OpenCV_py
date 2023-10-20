import numpy as py
import cv2 as cv

# contours, hierarchy = cv2.findContours(image, mode, methode)
# image：被检测的图像，必须是8位单通道二值图像。如果原始图像是彩色图像，必须转为灰度图像，并经过二值化处理
# mode：轮廓的检索模式
# methode：检测轮廓时使用的方法
# 返回值
# contours：检测出的所有轮廓，list类型，每一个元素都是某个轮廓的像素坐标数组
# hierarchy：轮廓之间的层次关系

# 通过findContours()方法找到图像轮廓后，为了方便开发人员观测，最好能把轮廓画出来，于是OpenCV提供了drawContours()方法用来绘制这些轮廓
# image = cv2.drawContours(image, contours, contourIdx, color, thickness, lineTypee, hierarchy, maxLevel, offset)
# image：被绘制轮廓的原始图像，可以是多通道图像
# contours：findContours()方法得出的轮廓列表
# contourIdx：绘制轮廓的索引，如果为-1则绘制所有轮廓
# color：绘制颜色，使用BGR格式
# thickness：可选参数，画笔的粗细程度，如果该值为-1则绘制实心轮廓
# lineTypee：可选参数，绘制轮廓的线型
# hierarchy：可选参数，findContours()方法得出的层次关系
# maxLevel：可选参数，绘制轮廓的层次深度，最深绘制第maxLevel层
# offse：可选参数，偏移量，可以改变绘制结果的位置
# 返回值
# image：同参数中的image，执行后原始图中就包含绘制的轮廓了，可以不使用此返回值保存结果

img1 = cv.imread('images/explosion.jpg')
img2 = cv.imread('images/explosion.jpg')

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
t, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # 灰度图像转化为二值图像
contours1, hierarchy1 = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # 检测所有轮廓
contours2, hierarchy2 = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) # 检测外轮廓
cv.drawContours(img1, contours1, -1, (0, 0, 255), 2)
cv.drawContours(img2, contours2, -1, (0, 0, 255), 2)
cv.imshow('img1', img1)
cv.imshow('img2', img2)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

# retval = cv2.boundingRect (array)
# array：轮廓数组
# 返回值
# retval：元组类型，包含4个整数值，分别是最小矩形包围框的：左上角顶点的横坐标、左上角顶点的纵坐标、矩形的宽和高。所以也可以写成x, y, w, h = cv2.boundingRect (array)的形式
# 
# center, radius = cv2.minEnclosingCircle(points)
# points：轮廓数组
# 返回值
# center：元组类型，包含2个浮点值，是最小圆形包围框圆心的横坐标和纵坐标
# radius：浮点类型，最小圆形包围框的半径

img = cv.imread('images/explosion.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
t, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # 对灰度图像进行二值化阈值处理
cv.imshow('binary', binary)
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv.boundingRect(contours[-1]) # 为什么是-1（倒数第一个），书上是0（正数第一个）
center , radius = cv.minEnclosingCircle(contours[-1])
x1 = int(round(center[0]))
y1 = int(round(center[1]))
cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv.circle(img, (x1, y1), int(radius), (0, 0, 255), 2)
cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()
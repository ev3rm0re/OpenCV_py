import cv2 as cv

# hull = cv2.convexHull(points, clockwise, returnPoints)
# points：轮廓数组
# clockwise：可选参数，布尔类型。当该值为True时，凸包中的点按顺时针排列，为False时按逆时针排列
# returnPoints：可选参数，布尔类型。当该值为True时返回点坐标，为False时返回点索引。默认值为True
# 返回值
# hull：凸包的点阵数组

img = cv.imread('images/explosion.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
t, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # 对灰度图像进行二值化阈值处理
cv.imshow('binary', binary)
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
hull = cv.convexHull(contours[-1])
cv.polylines(img, [hull], True, (0, 0, 255), 2)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
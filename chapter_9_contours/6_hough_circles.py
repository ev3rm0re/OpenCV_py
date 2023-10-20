import cv2 as cv
import numpy as np

# circles = cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
# image：检测的原始图像
# method：检测方法
# dp：累加器分辨率与原始图像分辨率之比的倒数。值为1时，累加器与原始图像具有相同的分辨率；值为2时，累加器的分辨率为原始图像的1/2。通常使用1作为参数
# minDist：圆心之间的最小距离
# param1：可选参数，Canny边缘检测使用的最大阈值
# param2：可选参数，检测圆环结果的投票数。第一轮筛选时投票数超过该值的圆环才会进入第二轮筛选。值越大，检测出的圆环越少，但越精准
# minRadius：可选参数，圆环的最小半径
# maxRadius：可选参数，圆环的最大半径
# 返回值
# circles：一个数组，元素为所有检测出的圆环，每个圆环也是一个数组，内容为圆心的横、纵坐标和半径长度，格式为：[[[x1 ,y1, r1], [x2 ,y2, r2]]]

img = cv.imread('images/coins.jpg')
o = img.copy()
o = cv.medianBlur(o, 5)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 70, param1=100, param2=25, minRadius=10, maxRadius=50)
circles = np.uint(np.around(circles)).astype(int)

for c in circles[0]:
    x, y, r = c
    cv.circle(img, (x, y), r, (0, 0, 255), 3)
    cv.circle(img, (x, y), 2, (0, 255, 0), 3)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()
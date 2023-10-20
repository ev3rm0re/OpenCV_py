import numpy as np
import cv2 as cv

canvas = np.ones((512, 512, 3), np.uint8) * 255
pts = np.array([[100, 50], [200, 50], [250, 250], [50, 250]], np.int32)
canvas = cv.polylines(canvas, [pts], True, (255, 0, 0), 5) 
# pts：由多边形各个顶点的坐标组成的一个列表，这个列表是一个numpy的数组类型

cv.imshow('canvas', canvas)

cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
import cv2 as cv

canvas = np.ones((512, 512, 3), np.uint8)
for i in range(0, 51):
    center_X = np.random.randint(0, 512)
    center_Y = np.random.randint(0, 512)
    radius = np.random.randint(11, 71)
    color = np.random.randint(0, 256, 3).tolist()
    cv.circle(canvas, (center_X, center_Y), radius, color, -1)
cv.imshow('canvas', canvas)

cv.waitKey(0)
cv.destroyAllWindows()

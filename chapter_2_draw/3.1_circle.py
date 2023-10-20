import numpy as np
import cv2 as cv

canvas = np.ones((512, 512, 3), np.uint8) * 255
canvas = cv.circle(canvas, (256, 256), 60, (0, 255, 0), 5)
canvas = cv.circle(canvas, (256, 256), 80, (0, 255, 0), 5)
canvas = cv.circle(canvas, (256, 256), 100, (0, 255, 0), 5)
cv.imshow('canvas', canvas)

cv.waitKey(0)
cv.destroyAllWindows()
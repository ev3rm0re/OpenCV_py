import numpy as np
import cv2 as cv

canvas = np.ones((512, 512, 3), np.uint8) * 255
canvas = cv.rectangle(canvas, (50, 50), (250, 250), (255, 0, 0), -1) # 最后一个参数-1代表实心
cv.imshow('canvas', canvas)

cv.waitKey(0)
cv.destroyAllWindows()
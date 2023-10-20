import numpy as np
import cv2 as cv

canvas = np.ones((512,512,3), np.uint8) * 255
canvas = cv.line(canvas, (50, 50), (250, 50), (255, 0, 0), 5)
canvas = cv.line(canvas, (50, 150), (250, 150), (0, 255, 0), 10)
canvas = cv.line(canvas, (50, 250), (250, 250), (0, 0, 255), 15)
canvas = cv.line(canvas, (150, 50), (150, 250), (0, 255, 255), 20)
cv.imshow("Lines", canvas)
cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
import cv2 as cv

width = 400
height = 400
img = np.random.randint(0, 256, (height, width, 3), 'uint8')
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
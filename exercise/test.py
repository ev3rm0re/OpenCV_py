import cv2
import numpy as np

img = cv2.imread('images/taylor.jpg')
canvas_x, canvas_y, ch = img.shape
canvas = np.zeros((canvas_x, canvas_y, 3), dtype=np.uint8)
mask = cv2.circle(canvas, (300, 250), 20, (255, 255, 255), -1)
roi = cv2.bitwise_and(img, mask)
cv2.imshow('canvas', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
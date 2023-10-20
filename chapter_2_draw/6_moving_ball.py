import numpy as np
import cv2 as cv
import time

width, height = 512, 512
radius = 20
x = radius + 20
y = radius + 100
x_offer, y_offer = 50, 25

while cv.waitKey(1) == -1:
    if x > width - radius or x < radius:
        x_offer *= -1
    if y > height - radius or y < radius:
        y_offer *= -1
    x += x_offer
    y += y_offer
    img = np.ones((width, height, 3), np.uint8) * 255
    cv.circle(img, (x, y), radius, (255, 0, 0), -1)
    cv.imshow('img', img)
    time.sleep(1/60)

cv.destroyAllWindows()
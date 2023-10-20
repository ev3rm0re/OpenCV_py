import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    light_black = np.array([0, 0, 0])
    deep_black = np.array([179, 255, 56])

    mask = cv.inRange(hsv, light_black, deep_black)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
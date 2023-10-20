import cv2 as cv
import numpy as np

e1 = cv.getTickCount()
img = cv.imread('roi.jpg')
bg = np.zeros((280, 450, 3), np.uint8)
bg[:] = (255, 255, 255)
cv.imshow('img', cv.addWeighted(img, 0.2, bg, 0.8, 0))
e2 = cv.getTickCount()
time = (e2 - e1)/cv.getTickFrequency()
print(time)


# h, w, c = img.shape
# print(h, w, c)
# print(img.dtype)
# img.itemset((10, 10, 2), 0)
# img.itemset((10, 10, 1), 0)
# cv.imshow('img', img)
# cv.imwrite('yellow-2.jpg', img)
cv.waitKey(0)
cv.destroyAllWindows()
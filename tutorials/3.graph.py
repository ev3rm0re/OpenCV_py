import numpy as np
import cv2 as cv
# 创建一个黑色的图像
img = np.zeros((512,512,3), np.uint8)
cv.circle(img, (255, 255), 50, (255, 0, 0), 5)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
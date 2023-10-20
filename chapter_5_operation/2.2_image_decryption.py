import numpy as np
import cv2 as cv

def cryption(img, img_key):
    return cv.bitwise_xor(img, img_key)

encoded = cv.imread('images/result.bmp')
key = cv.imread('images/key.bmp')

img = cryption(encoded, key)
cv.imshow('img', img)
cv.imwrite('images/decoded_taylor.jpg', img)

cv.waitKey(0)
cv.destroyAllWindows()
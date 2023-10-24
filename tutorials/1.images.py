import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('./images/taylor.jpg', 0)
    cv.imshow('image', img)
    k = cv.waitKey(0) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
    elif k == ord('s'):
        cv.imwrite('taylor_1.png', img)
        cv.destroyAllWindows()
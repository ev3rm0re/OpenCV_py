import cv2 as cv
import numpy as np

def cryption(img, img_key):
    return cv.bitwise_xor(img, img_key)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
video_key = np.random.randint(0, 256, (720, 1280, 3), np.uint8)
cv.imwrite('images/video_key.bmp',video_key)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('images/encoded.avi', fourcc, 30.0, (1280, 720))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame' ,frame)
        encoded = cryption(frame, video_key)
        cv.imshow('encoded', encoded)
        out.write(encoded)
        k = cv.waitKey(1)
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
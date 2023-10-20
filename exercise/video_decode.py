import cv2 as cv

def cryption(img, img_key):
    return cv.bitwise_xor(img, img_key)

cap = cv.VideoCapture('images/encoded.avi')
video_key = cv.imread('images/video_key.bmp')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        decoded = cryption(frame, video_key)
        cv.imshow('decoded', decoded)
        k = cv.waitKey(33)
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
import cv2 as cv

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720) # 720p摄像头
while (capture.isOpened()):
    ret, frame = capture.read()
    blur = cv.GaussianBlur(frame, (15, 15), sigmaX=0, sigmaY=0)
    if ret:
        cv.imshow('frame', frame)
        cv.imshow('blur', blur)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
            cv.imwrite('images/frame.jpg', frame)
            cv.imwrite('images/blur.jpg', blur)
    else:
        break
capture.release()
cv.destroyAllWindows()
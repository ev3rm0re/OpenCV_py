import cv2 as cv

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('images/output.avi', fourcc, 20.0, (640, 480))
while (capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        out.write(frame)
        cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
capture.release()
out.release()
cv.destroyAllWindows()
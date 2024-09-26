import cv2 as cv
import numpy as np
if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            copy = frame.copy()
            copy = cv.medianBlur(copy, 5)
            gray = cv.cvtColor(copy, cv.COLOR_BGR2GRAY)
            circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 70, param1=100, param2=50, minRadius=10, maxRadius=50)
            if circles is not None:
                circles = np.uint(np.around(circles)).astype(int)
                for c in circles[0]:
                    x, y, r = c
                    cv.circle(frame, (x, y), r, (0, 0, 0), 3)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == 27: # ESC key exits
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()
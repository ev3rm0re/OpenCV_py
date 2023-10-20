import cv2
import numpy as np
import time
if __name__ == "__main__":
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            height, width, ch = frame.shape
            descentre = 100
            rows_to_watch = 100
            crop_img = frame[int((height)/2+descentre):int((height)/2+(descentre+rows_to_watch))][0:int(width)]
            hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
            hsv = cv2.GaussianBlur(hsv, (5, 5), sigmaX=0, sigmaY=0)
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
            m = cv2.moments(mask, False)
            try:
                cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
            except ZeroDivisionError:
                cx, cy = height/2, width/2
            error_x = cx - width/2
            no_red = cv2.countNonZero(mask)
            if no_red > 10000:
                print(error_x)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.1)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
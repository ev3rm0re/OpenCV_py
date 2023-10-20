import cv2 as cv

# retval = cv2.VideoCapture.get(propId)
# retval：获取与propId对应的属性值
# propId：视频文件的属性值

capture = cv.VideoCapture(0)
while (capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        fps = capture.get(cv.CAP_PROP_FPS) # 帧率
        width = capture.get(cv.CAP_PROP_FRAME_WIDTH) # 宽度
        height = capture.get(cv.CAP_PROP_FRAME_HEIGHT) # 高度
        print('fps: {}, width: {}, height: {}'.format(fps, width, height))
        cv.imshow('frame', frame)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
capture.release()
cv.destroyAllWindows()
# OpenCV实现人脸检测需要做两步操作：加载级联分类器和使用分类器识别图像
# 1.加载级联分类器
# <CascadeClassifier object> = cv2.CascadeClassifier(filename)
# filename：级联分类器的XML文件名
# <CascadeClassifier object>：级联分类器对象
# 2.使用分类器识别图像
# objects = cascade.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
# cascade：已有的分类器对象
# image：待分析的图像
# scaleFactor：可选参数，扫描图像时的缩放比例
# minNeighbors：可选参数，每个候选区域至少保留多少个检测结果才可以判定为人脸。该值越大，分析的误差越小
# flags：可选参数，旧版本OpenCV的参数，建议使用默认值
# minSize：可选参数，最小的目标尺寸
# maxSize：可选参数，最大的目标尺寸
# 返回值
# objects：捕捉到的目标区域数组，数组中每一个元素都是一个目标区域，每一个目标区域都包含4个值，分别是：左上角点横坐标、左上角点纵坐标、区域宽、区域高。object的格式为：[[244　203　111　111]　[432　81　133　133]]

# D:/Program Files/Python39/Lib/site-packages/cv2/data/

import cv2 as cv

cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier('D:/Program Files/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        faces = cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.imshow('frame', frame)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

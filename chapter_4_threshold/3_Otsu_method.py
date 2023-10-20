import numpy as np
import cv2 as cv

# OpenCV提供了Otsu方法。Otsu方法能够遍历所有可能的阈值，从中找到最合适的阈值
# retval, dst = cv2.threshold(src, thresh, maxval, type)
# src：被处理的图像。需要注意的是，该图像需是灰度图像
# thresh：阈值，且要把阈值设置为0
# maxval：阈值处理采用的最大值，即255
# type：阈值处理类型。除在表8.1中选择一种阈值处理类型外，还要多传递一个参数，即cv2.THRESH_OTSU。例如，cv2.THRESH_BINARY+cv2.THRESH_OTSU
## 返回值
# retval：由Otsu方法计算得到并使用的最合适的阈值
# dst：经过阈值处理后的图像

img = cv.imread('images/taylorswift.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 转化为灰度图像
t1, dst1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY) # 二值化处理
t2, dst2 = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) # Ostu方法的阈值处理

cv.putText(dst2, "best threshold " + str(t2), (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) # 在图像上绘制最合适的阈值
cv.imshow('binary', dst1)
cv.imshow('otsu', dst2)

cv.waitKey(0)
cv.destroyAllWindows()
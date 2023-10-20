import numpy as np
import cv2 as cv

canvas = np.ones((512, 512, 3), np.uint8) * 255
cv.putText(canvas, "ev3rm0re", (20, 70), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 255, 0), 2)
#           (20, 70) - 文字在图中左下角坐标                 字体          字体大小   颜色    线条宽度
cv.putText(canvas, "ev3rm0re", (20, 200), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 255, 0), 2, 8, True) # 镜像文字


cv.imshow('canvas', canvas)

cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
import cv2 as cv

# result = cv2.matchTemplate(image, templ, method, mask)
# image：原始图像
# templ：模板图像，尺寸必须小于或等于原始图像
# method：匹配的方法
# mask：可选参数。掩模，只有cv2.TM_SQDIFF和cv2.TM_CCORR_NORMED支持此参数，建议采用默认值
# result：计算得出的匹配结果。如果原始图像的宽、高分别为W、H，模板图像的宽、高分别为w、h，result就是一个W-w+1列、H-h+1行的32位浮点型数组
# 数组中每一个浮点数都是原始图像中对应像素位置的匹配结果，其含义需要根据method参数来解读
# 单目标匹配
# minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(src, mask)
# src：matchTemplate()方法计算得出的数组
# mask：可选参数，掩模，建议使用默认值
# minValue：数组中的最小值
# maxValue：数组中的最大值
# minLoc：最小值的坐标，格式为(x, y)
# maxLoc：最大值的坐标，格式为(x, y)

img = cv.imread('images/background.jpg')
template = cv.imread('images/template.jpg')

height, width, channel = template.shape
results = cv.matchTemplate(img, template, cv.TM_SQDIFF_NORMED) # 按照标准平方差方式匹配

minValue, maxValue, minLoc, maxLoc = cv.minMaxLoc(results) # 获取匹配结果中的最小值、最大值、最小值坐标和最大值坐标
resultPoint1 = minLoc # 将最小值坐标当作最佳匹配区域的左上角坐标

resultPoint2 = (resultPoint1[0] + width, resultPoint1[1] + height)
cv.rectangle(img, resultPoint1, resultPoint2, (0, 0, 255), 2)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
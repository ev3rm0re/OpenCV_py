import cv2 as cv

image = []
image.append(cv.imread('images/taylor.jpg'))
image.append(cv.imread('images/taylorswift.jpg'))
template = cv.imread('images/taylor_template.jpg')
index= -1
min = 1
for i in range(0, len(image)):
    results = cv.matchTemplate(image[i], template, cv.TM_SQDIFF_NORMED)
    if min > any(results[0]): # min > any() 表示results第一行全为0（完全匹配）才能执行if分支
        index = i
cv.imshow('result', image[index])

cv.waitKey(0)
cv.destroyAllWindows()
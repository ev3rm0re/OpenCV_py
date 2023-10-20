import numpy as np
import cv2 as cv

# 异或运算还有一个特点：执行一次异或运算得到一个结果，再对这个结果执行第二次异或运算，则还原成最初的值
def cryption(img, img_key):
    return cv.bitwise_xor(img, img_key)

img = cv.imread('images/taylorswift.jpg')
rows, colmns, channels = img.shape # 原图像的行数、列数和通道数
img_key = np.random.randint(0, 256, (rows, colmns, 3), np.uint8) # 创建与原图像大小相等的随机像素图像，作为密钥

cv.imshow('img', img)
cv.imshow('img_key', img_key)
cv.imwrite('images/key.bmp', img_key) # 储存key格式要用bmp，无压缩，不然无法解码

result = cryption(img, img_key)
cv.imshow('result', result)
cv.imwrite('images/result.bmp', result) # 储存result格式也要用bmp，无压缩，不然无法解码

result = cv.imread('images/result.bmp')
img_key = cv.imread('images/key.bmp')

decode = cryption(result, img_key)
cv.imshow('decode', decode)
cv.imwrite('images/decode.jpg', decode)


cv.waitKey(0)
cv.destroyAllWindows()
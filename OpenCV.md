# OpenCV

## 一、图像入门

* 学习如何读取图像、如何显示图像以及如何将其保存起来
* 学习这些函数：**cv.imread()、cv.imshow()、cv.imwrite()**
* * 选择学习如何使用 Matplotlib 显示图像

```python
cv.imread()
cv.imshow()
cv.imwrite()
```

### 1.读取图像

* 使用 cv.imread() 函数读取一张图像，图片应该在工作目录中，或者应该提供完整的图像路径

```python
import numpy as np
import cv2 as cv
# 用灰度模式加载图像
img = cv.imread('messi5.jpg', 0)
```

* 第二个参数是一个 flag，指定了应该读取图像的方式
  * 1: 加载彩色图像，任何图像的透明度都会被忽略，它是默认标志
  * 0: 以灰度模式加载图像
  * -1: 加载图像，包括 alpha 通道

### 2.显示图像

* 用 cv.imshow() 函数在窗口中显示图像，窗口自动适应图像的大小。
* 第一个参数是窗口名，它是一个字符串，第二个参数就是我们的图像。你可以根据需要创建任意数量的窗口，但是窗口名字要不同。

```python
cv.imshow('image', img)
cv.waitKey(0) # cv.waitKey() 是一个键盘绑定函数，它的参数是以毫秒为单位的时间。该函数为任意键盘事件等待指定毫秒。如果传的是 0，它会一直等待键盘按下。
cv.destroyAllWindows() # 简单的销毁我们创建的所有窗口。如果你想销毁任意指定窗口，应该使用函数 cv.destroyWindow() 参数是确切的窗口名。
```

NOTE:

* 有一种特殊情况，你可以先创建一个窗口然后加载图像到该窗口。在这种情况下，你能指定窗口是否可调整大小。它是由这个函数完成的 **cv.namedWindow()**。默认情况下，flag 是 **cv.WINDOW_AUTOSIZE**。但如果你指定了 flag 为 **cv.WINDOW_NORMAL**，你能调整窗口大小。当图像尺寸太大，在窗口中添加跟踪条是很有用的。

```python
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
```

### 3.显示图像

* 保存图像，用这个函数 **cv.imwrite()**。第一个参数是文件名，第二个参数是你要保存的图像。


```python
cv.imwrite('messigray.png',img)
```

### 总结

```python
import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27: # ESC 退出
    cv.destroyAllWindows()
elif k == ord('s'): # 's' 保存退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()
```

* 注：如果你使用的是 64 位机器，你需要修改k = cv.waitKey(0)像这样：k = cv.waitKey(0) & 0xFF

### 4.使用Matplotlib

* Matplotlib 是一个 Python 的绘图库，提供了丰富多样的绘图函数

```python
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()
```

## 二、视频入门

* 学习加载视频、显示视频和保存视频
* 学习用相机捕捉并显示
* 学习这些函数：**cv.VideoCapture()，cv.VideoWriter()**

### 1.从相机捕捉视频

```python
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    # 一帧一帧捕捉
    ret, frame = cap.read()
    # 我们对帧的操作在这里
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示返回的每帧
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# 当所有事完成，释放 VideoCapture 对象
cap.release()
cv.destroyAllWindows()
```

* cap.read() 返回一个 bool 值(True/False)。如果加载成功，它会返回True。因此，你可以通过这个返回值判断视频是否结束

### 2.播放视频文件

* 它和从相机捕获一样，只需要用视频文件名更改相机索引。同时显示 frame，为 cv.waitKey() 使用合适的时间。

```python
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
```

### 3.保存视频

```python
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# 声明编码器和创建 VideoWrite 对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv.flip(frame,0)
        # 写入已经翻转好的帧
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放已经完成的工作
cap.release()
out.release()
cv.destroyAllWindows()
```

## 三、绘图功能

* 用 OpenCV 画不同的几何图形
* 学习这些函数：**cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText()** 等

### 1.画线

* 去画一条线，你需要传递线条的开始和结束的坐标

```python
import numpy as np
import cv2 as cv
# 创建一个黑色的图像
img = np.zeros((512,512,3), np.uint8)
# 画一条 5px 宽的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),5)
```

### 2.画矩形

* 画一个矩形，你需要矩形的左上角和右下角

```python
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
```

### 3.画圆

* 画一个圆，你需要它的圆心和半径

```python
cv.circle(img,(447,63), 63, (0,0,255), -1)
```

### 4.画椭圆

* 画一个椭圆，你需要传好几个参数。一个参数是圆心位置 (x,y)。下个参数是轴的长度 (长轴长度，短轴长度)。角度是椭圆在你逆时针方向的旋转角度。startAngle 和 endAngle 表示从长轴顺时针方向测量的椭圆弧的起点和终点

```python
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
```


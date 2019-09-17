import cv2
import numpy
img = cv2.resize(cv2.imread('.//picture.jpg'), (640, 480))  # 读取图像
b, g, r = cv2.split(img)  # 拆分通道
# 单独显示每个通道
cv2.imshow('B', b)
cv2.imshow('G', g)
cv2.imshow('R', r)

# 以bgr,合并显示
rows, cols, chn = img.shape
b = cv2.split(img)[0]
g = numpy.zeros((rows, cols), img.dtype)
r = numpy.zeros((rows, cols), img.dtype)
cv2.imshow('merge', cv2.merge([b, g, r]))

# 等待响应，结束时销毁窗口
cv2.waitKey()
cv2.destroyAllWindows()


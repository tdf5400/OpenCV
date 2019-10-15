import cv2
import numpy as np

"""
Sobel操作（得到边缘图像）
    边缘图像 = Sobel(dx=?,dy=0) + Sobel(dx=0,dy=?)
    函数 Sobel
    sobel = cv2.Sobel(src, deepth, dx, dy, [ksize])
        [注]: ksize 默认为3x3，若为负数则使用scharr算子
        因为数据为uint8，为了避免只有一个边缘的情况（只能大于等于0），
        计算时deepth一般为 cv2.CV_64F，运算完成再取绝对值转回uint8。
        转回uint8的函数为 cv2.convertScaleAbs(src) 
"""

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))

dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)           # 处理
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
dx = cv2.convertScaleAbs(dx)            # 转回uint8
dy = cv2.convertScaleAbs(dy)
sobel = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)   # 以权值相加
cv2.imshow('Sobel', sobel)


"""
scharr操作（得到边缘图像[比sobel算子准确度更高]） （用法与sobel算子相似）
    边缘图像 = Scharr(dx=?,dy=0) + Scharr(dx=0,dy=?)
    函数 Scharr
    dst = cv2.Scharr(src, deepth, dx, dy)
        [注]：应满足条件 dx>=0 && dy>=0 && dx+dy==1
        因为数据为uint8，为了避免只有一个边缘的情况（只能大于等于0），
        计算时deepth一般为 cv2.CV_64F，运算完成再取绝对值转回uint8。
        转回uint8的函数为 cv2.convertScaleAbs(src) 
"""
dx = cv2.Scharr(img, cv2.CV_64F, 1, 0)           # 处理
dy = cv2.Scharr(img, cv2.CV_64F, 0, 1)
dx = cv2.convertScaleAbs(dx)            # 转回uint8
dy = cv2.convertScaleAbs(dy)
scharr = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)   # 以权值相加

cv2.imshow('Scharr', scharr)



cv2.waitKey(0)
cv2.destroyAllWindows()

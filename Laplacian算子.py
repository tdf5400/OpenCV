import cv2
import numpy as np

"""
Laplacian操作（得到边缘图像）
    函数 Laplacian
    dst = cv2.Laplacian(src, deepth)
"""

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))

laplacian = cv2.Laplacian(img, cv2.CV_64F)           # 处理
laplacian = cv2.convertScaleAbs(laplacian)            # 转回uint8
cv2.imshow('laplacian', laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

"""
礼帽操作（得到噪声图像）
    礼帽图像 = 原始图像 - 开运算图像
    函数 morphologyEx
    result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    
"""
img = cv2.resize(cv2.imread('./picture.jpg'), (640, 480))
kernel = np.ones((5, 5), dtype=np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('Demo', img - tophat)
cv2.imshow('Tophat', tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()

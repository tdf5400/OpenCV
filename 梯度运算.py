import cv2
import numpy as np

"""
梯度运算（出边缘）
    图像膨胀 - 图像腐蚀
    函数 morphologyEx
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
"""

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))
kernel = np.array(((1, 1, 1),
                    (1, 1, 1),
                    (1, 1, 1)), dtype=np.uint8)

erode = cv2.erode(img, kernel, iterations=1)    # 腐蚀
dilation = cv2.dilate(img, kernel, iterations=1)    # 膨胀
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)    # 梯度运算

cv2.imshow('Demo', img)
# cv2.imshow('Erode', erode)
# cv2.imshow('Dilation', dilation)
cv2.imshow('Gradient_0', dilation - erode)  # 梯度运算(相减实现)
cv2.imshow('Gradient_1', gradient)  # 梯度运算(OPENCV实现)


cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

"""
Canny边缘检测（得到边缘图像）（边缘信息数量可控）
    Canny = 去噪 → 梯度 → 非极大值抑制 → 滞后阈值
    函数 Canny
    deges = cv2.Canny(img, threshold1, threshold2)
        deges - 边界图像
        threshold1 - minVal最小阈值
        threshold2 - maxVal最大阈值
"""

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))

# 阈值都比较大 -> 细节少
canny_Low = cv2.Canny(img, 100, 200)
cv2.imshow('Canny_Low', canny_Low)
# 阈值都比较小 -> 细节多
canny_More = cv2.Canny(img, 10, 80)
cv2.imshow('Canny_More', canny_More)

cv2.waitKey(0)
cv2.destroyAllWindows()

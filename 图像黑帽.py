import cv2
import numpy as np

"""
黑帽操作（得到图像内部的小孔，或前景色中的小黑点）
    黑帽图像 = 开运算图像 - 原始图像 （与礼帽运算顺序相反）
    函数 morphologyEx
    result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

"""
img = cv2.resize(cv2.imread('./test_salt.jpg'), (640, 480))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3, 3), dtype=np.uint8)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Raw', img)
cv2.imshow('Blackhat', blackhat)
cv2.imshow('Reduce', img + blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))
equ = cv2.equalizeHist(img)
# plt.hist(img.ravel(), 256)
# plt.figure()                # 新建窗口
# plt.hist(equ.ravel(), 256)
#
# cv2.imshow('img', img)
# cv2.imshow('equ', equ)
# plt.show()

# 使用subplot函数绘制
plt.subplot(121)
plt.hist(img.ravel(), 256)
plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), 256)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

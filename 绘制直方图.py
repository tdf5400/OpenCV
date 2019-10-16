import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('./picture.jpg'), (640, 480))
cv2.imshow('image', img)
# 使用matplotlib绘制
# plt.hist(img.ravel(), 256)
# plt.show()

# 使用OPENCV
# histb = cv2.calcHist([img], [0], None, [256], [0, 255])
# histg = cv2.calcHist([img], [1], None, [256], [0, 255])
# gistr = cv2.calcHist([img], [2], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
# plt.plot(gistr, color='r')
# plt.show()

# 使用掩膜
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros(img.shape, np.uint8)
mask[200:400, 200:400] = 255
histMI = cv2.calcHist([img], [0], mask, [256], [0, 255])
plt.plot(histMI)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

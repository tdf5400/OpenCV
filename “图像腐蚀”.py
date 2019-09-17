import cv2
import numpy as np

img = cv2.resize(cv2.imread('.//picture.jpg'), (640, 480))
kernel = np.ones((5,5), np.uint8)
# 腐蚀
erosion = cv2.erode(img, kernel, iterations=1)  # 腐蚀次数=1
# 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)
# 开运算（先进行腐蚀再进行膨胀）[可用来去除噪声]
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 闭运算（先膨胀再腐蚀）[用来填充前景物体的小洞]
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Demo', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# _*_ coding:utf-8 _*_
import numpy as np
import cv2

img = cv2.resize(cv2.imread('./picture.jpg'), (640, 480))

# 转灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow('Binary', binary)

# 距离变换
dist = cv2.distanceTransform(binary, cv2.DIST_L2, 3)
dist_output = cv2.normalize(dist, 0, 1.0, cv2.NORM_MINMAX)
cv2.imshow('distance-t', dist_output*50)

# 取种子
ret, surface = cv2.threshold(dist, dist.max()*0.6, 255, cv2.THRESH_BINARY)
cv2.imshow('surface-bin', surface)

surface_fg = np.uint8(surface)
unknown = cv2.subtract(binary, surface_fg)
ret, markers = cv2.connectedComponents(surface_fg)
print(ret)

# 分水岭
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(img, markers=markers)
img[markers == -1] = [0, 0, 255]
cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))

# 向下取样
down = cv2.pyrDown(img)
cv2.imshow("pyrDown", down)
# 向上取样
up = cv2.pyrUp(img)
cv2.imshow("pyrUp", up)
# 拉普拉斯金字塔
od = cv2.pyrDown(img)
odu = cv2.pyrUp(od)
lapPyr = img - odu
cv2.imshow('Orginal', img)
cv2.imshow('lapPyr', lapPyr)
demo = cv2.add(lapPyr, cv2.medianBlur(img, 3))
cv2.imshow('demo', demo)

cv2.waitKey(0)
cv2.destroyAllWindows()

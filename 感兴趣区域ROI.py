import cv2

img = cv2.imread('.//picture.jpg')
img = cv2.resize(img, (640, 480))

block = img[300:600, 100:200]  # 截取区域
img[300:600, 0:100] = block  # 填充区域

# 显示结果
cv2.namedWindow('Demo')
cv2.resizeWindow('Demo', 640, 480)
cv2.imshow('Demo', img)
# cv2.imshow('Demo_1', block)

cv2.waitKey(0)

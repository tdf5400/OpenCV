# _*_ coding: utf-8 _*_
import numpy as np
import cv2


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], dtype=np.uint8)     # mask为行和列都加2

    cv2.floodFill(copyImg, mask, (240, 0), (0,0, 255))
    cv2.imshow("fill_color_demo", copyImg)


img = cv2.imread('./picture.jpg')
img = cv2.resize(img, (640, 480))
cv2.imshow('input_image', img)
fill_color_demo(img)

cv2.waitKey(0)
cv2.destroyAllWindows()

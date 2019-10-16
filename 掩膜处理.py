import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('./picture.jpg'), (640, 480))
mask = np.zeros(img.shape, np.uint8)
mask[200:400, 200:400] = 255
mi = cv2.bitwise_and(img, mask)
cv2.imshow('Demo', mi)

cv2.waitKey(0)
cv2.destroyAllWindows()

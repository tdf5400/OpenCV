import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('./picture.jpg'), (640, 480))
# 重新排列图层（BGR→RGB）
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
# 显示图像
plt.subplot(121)    # 设定框
plt.imshow(img)     # 载入图片
plt.axis('off')     # 关闭坐标系

plt.subplot(122)
plt.imshow(img2)
plt.axis('off')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np
import cv2
from matplotlib import pyplot as plt

# 创建点集合
x = np.random.randint(25, 100, (25, 2))
y = np.random.randint(60, 85, (25, 2))
points = np.vstack((x, y))
points = np.float32(points)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(points, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Output:
#       ret - 形状
#       label - 相应点的分组数据
#       center - 中心点
# Input:
#       1. points - 点的集合
#       2. 3 - 三个分类
#       3. None - 分组数据集合（此处为空）
#       4. criteria - 迭代位移小于criteria时终止
#       5. 10 - 迭代次数
#       6. cv2.KMEANS_RANDOM_CENTERS - 中心点寻找方式（此处为随机）

# Now separate the data, Note the flatten()
A = points[label.ravel() == 0]
B = points[label.ravel() == 1]
C = points[label.ravel() == 2]

# Plot the data
plt.scatter(A[:, 0], A[:, 1], c='g')
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(C[:, 0], C[:, 1], c='b')
plt.scatter(center[:, 0], center[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()



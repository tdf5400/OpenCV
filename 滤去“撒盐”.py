import cv2
import numpy

cleanCore = ((0, -1, 0), (-1, 3, -1), (0, -1, 0))  # 扫描核
# 获取cleanCore形状及中心点
stepRows, stepCols = numpy.shape(cleanCore)
stepCenter = (int(stepRows/2+0.5), int(stepCols/2+0.5))
# 读取照片
img = cv2.imread('.//test_salt.jpg')
imgRows, imgCols, = img.shape
# 扫描
for x in range(stepCenter[0], imgRows-stepRows):  # 移动准心
    for y in range(stepCenter[1], imgCols-stepCols):
        # 核内部扫描
        for rows in range(stepRows):
            for stepCols in range(stepCols):
              score = img.item()


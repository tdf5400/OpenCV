import cv2
import numpy

img = cv2.imread("./picture.jpg")  # 加载图片

# cv2.namedWindow("Image")  # 创建名称为"Image"的窗口

img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图片转化为黑白
# cv2.imshow("Image", img_1)  # 将图片发送到"Image"窗口

# 保存图片（低质量）（100为最高质量）
# cv2.imwrite("./test_LowQuality.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 0])
# 保存图片（高压缩）（9为最高压缩级别）
# cv2.imwrite("./test_HighCompression.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])


cv2.waitKey(0)  # 等待输入
cv2.destroyAllWindows()  # 释放窗口



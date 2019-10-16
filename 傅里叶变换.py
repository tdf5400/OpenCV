import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('./picture.jpg', cv2.IMREAD_GRAYSCALE), (640, 480))
"""
使用numpy实现
"""
# # 进行傅里叶变换
# f = np.fft.fft2(img)            # 进行傅里叶变换
# fshift = np.fft.fftshift(f)     # 移动中心位置
# result = 20*np.log(np.abs(fshift))  # 调整值范围
# # 显示原图
# plt.figure(figsize=(100, 100))
# plt.subplot(221)
# plt.imshow(img, cmap='gray')
# plt.title('original')
# plt.axis('off')
# # 显示结果
# plt.subplot(222)
# plt.imshow(result, cmap='gray')
# plt.title('result')
# plt.axis('off')
#
# # 在此处进行高通滤波
# rows, cols = img.shape
# crow, ccol = int(rows/2), int(cols/2)           # 取中心点
# fshift[crow-30:crow+30, ccol-30:ccol+30] = 0    # 将中心60*60的范围变成黑色
#
# # 进行逆傅里叶变换
# ishift = np.fft.ifftshift(fshift)   # 从中间移回去
# iimg = np.fft.ifft2(ishift)         # 逆傅里叶变换
# iimg = np.abs(iimg)                 # 将复数数组转换为实数
# plt.subplot(223)
# plt.imshow(iimg, cmap='gray')
# plt.title('iimg')
# plt.axis('off')
#
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""
使用OPENCV实现
"""
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)                # 傅里叶变换
dftShift = np.fft.fftshift(dft)                                            # 移动高低频
result = 20*np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))     # 调整值范围（计算幅度）

# 显示原图
plt.figure(figsize=(100, 100))
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')
# 显示结果
plt.subplot(222)
plt.imshow(result, cmap='gray')
plt.title('result')
plt.axis('off')

# 低通滤波
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows, cols, 2), np.uint8)  # 生成掩膜
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fshift = dftShift*mask  # 生效掩膜


# 进行逆傅里叶变换
ishift = np.fft.ifftshift(fshift)     # 移回高低频
ilmg = cv2.idft(ishift)                 # 逆傅里叶计算
ilmg = cv2.magnitude(ilmg[:, :, 0], ilmg[:, :, 1])  # 值域转换
plt.subplot(223)
plt.imshow(ilmg, cmap='gray')
plt.title('inverse')
plt.axis('off')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

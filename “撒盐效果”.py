import cv2
import random


def putSalt(__img, __mount):
    """
    进行“撒盐”
    :param __img:输入图像
    :param __mount:撒盐数量
    :return:修改后的图像
    """
    if __mount > 0:
        for i in range(0, __mount):
            __img[random.randint(0, 480 - 1), random.randint(0, 640 - 1)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return __img


def colorChange(__img, __color, __deviation):
    """
    改变颜色偏移值
    :param __img: 输入图像
    :param __color: 调整的目标颜色
    :param __deviation: 偏移值
    :return:修改后的图像
    """
    colorCode = {'B': 0, 'G': 1, 'R': 2}
    step = 0  # 计步
    # size = __img.cv2.wide()
    size = __img.shape  # 获取图像形状，返回行数，列数，通道数的元组
    mount = int(__img.size / 3)  # 获取单通道数量
    for i in range(size[0]):
        for j in range(size[1]):
            # 读取像素点
            cache = __img.item(i, j, colorCode[__color])
            # 设置调整范围0-255
            if (cache + __deviation) >= 255:
                cache = 255
            elif (cache + __deviation) <= 0:
                cache = 0
            else:
                cache += __deviation
            # 更改颜色值
            __img.itemset((i, j, colorCode[__color]), cache)

            # 计步增加
            step += 1
            print(f'Step:{step}/{mount}')
    return __img


# 加载图像并更改图片分辨率
img = cv2.resize(cv2.imread("./picture.jpg"), (640, 480))
# 对图像进行处理
# img = colorChange(img, 'R', -255)
img = putSalt(img, 10000)
# 创建窗口
cv2.namedWindow("Output Demo")
# 定义窗口大小
cv2.resizeWindow("Output Demo", 640, 480)
# 输出图片
cv2.imshow("Output Demo", img)

cv2.waitKey(0)

# 保存图片
cv2.imwrite("./test_salt.jpg", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# %%

import cv2
import numpy as np


# %%

# 图像校正
def Correct(img_):
    # 输入相机标定获得的内参矩阵
    cameraMatrix = np.array([[1.19769323e+04, 0.00000000e+00, 2.50220317e+03],
                             [0.00000000e+00, 1.19809702e+04, 1.58893661e+03],
                             [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    # 输入相机标定获得的畸变矩阵
    distCoeffs = np.array([[2.53833497e-02, -1.40871016e+00, 6.71690878e-04,
                            -2.49641770e-04, 1.87367485e+01]])

    # 获得图像尺寸 行(高) 列(行)
    h, w = img_.shape[:2]

    # 矫正图像
    # cv2.initUndistortRectifyMap()函数和 cv2.remap()函数
    map1, map2 = cv2.initUndistortRectifyMap(cameraMatrix, distCoeffs, None, None, (w, h), 5)
    result = cv2.remap(img_, map1, map2, cv2.INTER_LINEAR)

    return result

#自适应均值模糊
def adaptiveThresh(I, winSize, ratio=0.15):
    # 第一步:对图像矩阵进行均值平滑
    I_mean = cv2.boxFilter(I, cv2.CV_32FC1, winSize)

    # 第二步:原图像矩阵与平滑结果做差
    out = I - (1.0 - ratio) * I_mean

    # 第三步:当差值大于或等于0时，输出值为255；反之，输出值为0
    out[out >= 0] = 255
    out[out < 0] = 0
    out = out.astype(np.uint8)
    return out

#找点
def Contour(img_):

    img_new = Correct(img_)
    img_new = cv2.GaussianBlur(img_new, (15, 15), 0, 0)
    gray = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)
    t, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    ls = []
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for k in range(len(contours)):
        if len(contours[k]) < 600 or k == len(contours) - 1:
            continue
        # cv2.drawContours(img_new, contours[k], -1, (0, 0, 255), 10)
        ls.append(k)
    '''img_new = cv2.resize(img_new, (684, 456))
    cv2.imshow("img", img_new)'''
    return ls, contours

def ContourFitting(image):
    ls, contours = Contour(image)

    x1, y1, x2, y2, x3, y3, xy, x2y, xy2 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    L = []
    for i in ls:
        for j in range(len(contours[i])):
            # 坐标缩小1824倍，防止数据溢出
            x = contours[i][j][0][0] / 1824
            y = contours[i][j][0][1] / 1824

            x1 = (x1 + x)
            y1 = (y1 + y)
            x2 = (x2 + pow(x, 2))
            y2 = (y2 + pow(y, 2))
            x3 = (x3 + pow(x, 3))
            y3 = (y3 + pow(y, 3))
            xy = (xy + x * y)
            x2y = (x2y + pow(x, 2) * y)
            xy2 = (xy2 + x * pow(y, 2))

        a, b, r = Algorithm(len(contours[i]), x1, y1, x2, y2, x3, y3, xy, x2y, xy2)
        x1, y1, x2, y2, x3, y3, xy, x2y, xy2 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        L.append(((a, b), r * 1824))
    return L

# 拟合，求直径算法
def Algorithm(N, x1, y1, x2, y2, x3, y3, xy, x2y, xy2):
    C = N * x2 - pow(x1, 2)
    D = N * xy - x1 * y1
    E = N * x3 + N * xy2 - (x2 + y2) * x1
    G = N * y2 - pow(y1, 2)
    H = N * x2y + N * y3 - (x2 + y2) * y1

    # 算出原始圆心和半径
    a = (H * D - E * G) / ((C * G - D * D) * (-2))
    b = (H * C - E * D) / ((D * D - G * C) * (-2))
    c = -(a * x1 + b * y1 + x2 + y2) / N
    # r = int(((pow(a, 2) + pow(b, 2) - 4 * c) ** 0.5) / 2)
    r = ((x2 + y2) / N + a ** 2 + b ** 2 - (2 * a * x1 + 2 * b * y1) / N) ** 0.5
    a = int(a * 1824)
    b = int(b * 1824)

    return a, b, r


# %%

# 计算直径实际长度
def Length(r):
    R = 2 * r
    L = R * 0.0145  # 0.0145是转换参数
    return L


# %%

# 判断是否符合要求
def Compare(image_, l1, l2):
    L = ContourFitting(image_)

    # 获得矫正过后的图像
    img = Correct(image_)

    # 判断并打印

    # 筛选，去掉无关的拟合圆
    k = L.copy()
    n = 0
    for i in k:
        for j in k:
            if abs(i[0][1] - j[0][1]) < 60:
                n += 1
        if n != 3:
            L.remove(i)
        n = 0

    p = L.copy()
    for i in p:
        if 1200 < i[0][1] < 3100:
            L.remove(i)

    # print(L)

    result = []

    for i in L:
        item = []
        if abs(Length(i[1]) - l1) <= 0.03 and i[0][1] < 2000:
            cv2.circle(img, i[0], int(i[1]), (0, 255, 0), 5)
            cv2.putText(img, 'R:{:.3f},yes'.format(Length(i[1])), (i[0][0] - 200, i[0][1] - 200),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        4, (0, 255, 0), 12)
            item.append(round(abs(Length(i[1]) - l1),2))
            item.append(round(Length(i[1]),3))
            item.append(1)
        elif abs(Length(i[1]) - l2) <= 0.03 and i[0][1] > 2000:
            cv2.circle(img, i[0], int(i[1]), (0, 255, 0), 5)
            cv2.putText(img, 'R:{:.3f},yes'.format(Length(i[1])), (i[0][0] - 200, i[0][1] - 200),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        4, (0, 255, 0), 12)
            item.append(round(abs(Length(i[1]) - l2),2))
            item.append(round(Length(i[1]),3))
            item.append(1)
        else:
            cv2.circle(img, i[0], int(i[1]), (0, 0, 255), 5)
            cv2.putText(img, 'R:{:.3f},no'.format(Length(i[1])), (i[0][0] - 200, i[0][1] - 200),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        4, (0, 0, 255), 12)
            item.append(round(abs(Length(i[1]) - l1)))
            item.append(round(Length(i[1]),3))
            item.append(-1)
        result.append(item)

    # img = cv2.resize(img, (684, 456))
    # cv2.imshow("1", img)
    # cv2.waitKey()
    return img,result


# # %%
#
# def main1(a, b):
#     img = cv2.imread("test.png")
#     result = Compare(img, a, b)
#     print(result)
#     cv2.destroyAllWindows()
#
#
# # A, B = input("输入第一行和第二行圆孔的直径,空格间隔\n").split(' ')
# if __name__ == '__main__':
#     main1(3.2, 4)




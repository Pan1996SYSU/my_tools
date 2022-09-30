import cv2
from sonic.utils_func import cv_img_read
import numpy as np
def coordinate_rotation_transformation(point, mat=[[1, 0, 0], [0, 1, 0]]):
    new_point = np.dot(mat, np.array([[point[0]], [point[1]], [1]]))
    return new_point
'''
self.A1_weld_area = [255, 50, 350, 1250]
self.A2_weld_area = [210, 50, 310, 1220]
self.B1_weld_area = [220, 50, 330, 2200]
self.B2_weld_area = [220, 50, 310, 2150]
'''
# img = cv_img_read(
#     r"D:\桌面\顶盖焊\后处理\20220831-164036_dgh_0822OK图像\NG\raw\A1\C0-08ICB2500107DAC8N0800734-A1-2022082208532794-G.tiff")
# cv2.rectangle(img, (255, 50), (350, 1250), (255, 0, 0), -1)
# cv2.namedWindow('img', 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# img = cv_img_read(r"D:\桌面\顶盖焊\后处理\20220831-164036_dgh_0822OK图像\NG\raw\A2\C0-08ICB2500107DAC8N0800729-A2-2022082208495936-G.tiff")
# cv2.rectangle(img, (210, 50), (310, 1220), (255, 0, 0), -1)
# cv2.namedWindow('img', 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)
#
# img = cv_img_read(r"D:\桌面\顶盖焊\后处理\20220831-164036_dgh_0822OK图像\NG\raw\B1\C0-08ICB2500107DAC8N0800738-B1-2022082208592504-G.tiff")
# p1 = (220, 50)
# p2 = (330, 2200)
# # h, w = img.shape[:2]
# # center = (w // 2, h // 2)
# # # 旋转中心坐标，逆时针旋转：45°，缩放因子：0.5
# # M_1 = cv2.getRotationMatrix2D(center, -1.8, 1)
# # img = cv2.warpAffine(img, M_1, (w, h))
# # p1 = coordinate_rotation_transformation(p1, M_1)
# # p2 = coordinate_rotation_transformation(p2, M_1)
# cv2.rectangle(img, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), (255, 0, 0), -1)
# cv2.namedWindow('img', 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# print(123)
# #
img = cv_img_read(r"D:\桌面\顶盖焊\后处理\20220831-164036_dgh_0822OK图像\NG\raw\B2\C0-08ICB2500107DAC8N0800769-B2-2022082212521055-G.tiff")
cv2.rectangle(img, (220, 50), (310, 2150), (255, 0, 0), -1)
cv2.namedWindow('img', 0)
cv2.imshow('img', img)
cv2.waitKey(0)

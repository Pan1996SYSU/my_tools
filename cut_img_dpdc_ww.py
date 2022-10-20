import cv2
import halcon as ha
import numpy as np
from scipy.spatial import distance
from sonic.utils_func import cv_img_read, glob_extensions

input_path = r"D:\桌面\20220930-NG图"
t_img_path = r"D:\桌面\20220930-NG图\NG_Image5\WeldSpecial\Right_Weld2D\L\0JBMBPE6M106EDC9Y3300060_0022_10-06-11-22_Lum.tiff"


def create_model_id(template_img_path):
    Image = ha.read_image(template_img_path)
    ROI = ha.gen_circle(1530.96, 589.608, 93.5595)
    ImageReduced = ha.reduce_domain(Image, ROI)
    # 根据剪裁的模板图像创建基于形状的模板，返回模板句柄ShapeModelID
    Edges = ha.edges_sub_pix(ImageReduced, 'canny', 8, 40, 60)
    ModelID = ha.create_shape_model_xld(
        Edges, 'auto', -180, 180, 'auto', 'auto', 'ignore_local_polarity', 1)
    return ModelID


def find_2_dim_min_index(dis_mat):
    m, n = dis_mat.shape
    index = int(dis_mat.argmin())
    col = int(index / n)
    row = index % n
    return col, row


if __name__ == '__main__':
    model_ID = create_model_id(t_img_path)
    img_path_list = glob_extensions(input_path)
    j = 0
    for img_path in img_path_list:
        SearchImage = ha.read_image(img_path)
        Row, Column, Angle, Scale, Score1, Model = ha.find_scaled_shape_models(
            SearchImage, model_ID, -180, 180, 1, 1, 0.5, 4, 0, 'least_squares',
            0, 0.9)

        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        # config可自定义
        p = [(w // 2, h // 2)]
        points = []
        for x, y in zip(Column, Row):
            points.append([x, y])

        # 求点集中的距离矩阵，如果有两个相距小于700的点，剔除得分低的点
        dis_matrix1 = distance.cdist(points, points, 'euclidean')
        dis_matrix1[dis_matrix1 == 0] = 2000
        while np.min(dis_matrix1) < 700:
            c, r = find_2_dim_min_index(dis_matrix1)
            if Score1[c] > Score1[r]:
                points = np.delete(points, r, axis=0)
                Score1 = np.delete(Score1, r)
            else:
                points = np.delete(points, c, axis=0)
                Score1 = np.delete(Score1, c)
            dis_matrix1 = distance.cdist(points, points, 'euclidean')
            dis_matrix1[dis_matrix1 == 0] = 2000

        # 求离图片中心最近的两个点
        dis_matrix2 = distance.cdist(p, points, 'euclidean')

        if dis_matrix2.size != 0:
            min_index = np.argmin(dis_matrix2)
            x = int(points[min_index][0])
            y = int(points[min_index][1])
            cv2.circle(img, (x, y), 50, 0, -1)

            dis_matrix2 = np.delete(dis_matrix2, min_index)
            points = np.delete(points, min_index, axis=0)
        if dis_matrix2.size != 0:
            min_index = np.argmin(dis_matrix2)
            x = int(points[min_index][0])
            y = int(points[min_index][1])
            cv2.circle(img, (x, y), 50, 0, -1)

        # cv2.namedWindow('img', 0)
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        cv2.imencode('.tiff', img)[1].tofile(f'D:\桌面\pth/{j}.tiff')
        j += 1

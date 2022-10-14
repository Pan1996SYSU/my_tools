import os.path
import traceback
from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read

input_path = r"D:\桌面\20221014"
template_path = r'D:/桌面/20221014/1/10_14_12_00_27_844.676_NG.bmp'
output_path = r"D:\桌面\img"
output_path = Path(output_path)
img_path_list = glob_extensions(input_path)

T_Image = ha.read_image(template_path)
ROI = ha.gen_rectangle1(1058.12, 1861.42, 1173.62, 1959.52)
ImageReduced = ha.reduce_domain(T_Image, ROI)
ModelImages, ModelRegions = ha.inspect_shape_model(ImageReduced, 1, 30)
Edges = ha.edges_sub_pix(ImageReduced, 'canny', 1.2, 60, 90)
ModelID = ha.create_shape_model_xld(
    Edges, 'auto', 0, 360, 'auto', 'auto', 'ignore_local_polarity', 5)

y_edge = 200
x_edge = 250
num = len(img_path_list)
n = num // 20

for j, img_path in enumerate(img_path_list):
    if j % num == 0:
        print(f'{j / num * 100}%')
    try:
        Image = ha.read_image(img_path)
        Row, Column, Angle, Scale, Score1, Model = ha.find_scaled_shape_models(
            Image, ModelID, 0, 360, 0.97, 1.03, 0.7, 1, 0.5, 'least_squares',
            0, 0.9)
        img_path = Path(img_path)
        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        for i in range(len(Row)):
            try:
                y = int(Row[0])
                x = int(Column[0])
                crop_img = img[max(0, y - y_edge):min(h, y + y_edge),
                               max(0, x - x_edge):min(w, x + x_edge)].copy()
                img_output_path = Path(
                    output_path, img_path.relative_to(input_path))
                if not os.path.exists(img_output_path.parent):
                    os.makedirs(img_output_path.parent)
                img_name = os.path.basename(img_output_path).split('.')[0]
                img_suffix = os.path.basename(img_output_path).split('.')[-1]
                cv2.imencode(f'.{img_suffix}', crop_img)[1].tofile(
                    f'{img_output_path.parent}/{img_name}_{i}.{img_suffix}')
            except Exception as e:
                print(e)
                print(traceback.format_exc())
    except Exception as e:
        print(e)
        print(traceback.format_exc())
print(f'{num / num * 100}%')

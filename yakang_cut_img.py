import os.path
import traceback
from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read

input_path = r"Z:\2-现场取图\CYS.210711-雅康卷绕一体机-麻点寻边\20220912"
output_path = r"D:\桌面\img"
output_path = Path(output_path)
img_path_list = glob_extensions(input_path)

edge = 150
num = len(img_path_list)
for j, img_path in enumerate(img_path_list):
    if j % 10 == 0:
        print(f'{j / num * 100}%')
    try:
        Image = ha.read_image(img_path)
        Red, Green, Blue = ha.decompose3(Image)
        Regions = ha.threshold(Green, 226, 255)
        ImageReduced = ha.reduce_domain(Image, Regions)
        ImageReducedChannel3 = ha.access_channel(ImageReduced, 3)
        Regions1 = ha.threshold(ImageReducedChannel3, 138, 255)
        RegionOpening = ha.opening_rectangle1(Regions1, 2, 2)
        RegionClosing1 = ha.closing_rectangle1(RegionOpening, 2, 2)
        RegionClosing = ha.closing_rectangle1(RegionClosing1, 300, 50)
        RegionOpening1 = ha.opening_rectangle1(RegionClosing, 100, 100)
        RegionDifference = ha.difference(RegionClosing, RegionOpening1)
        ConnectedRegions = ha.connection(RegionDifference)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'area', 'and', 8500, 25000)
        SelectedRegions1 = ha.select_shape(
            SelectedRegions, 'inner_height', 'and', 50, 90)
        SelectedRegions2 = ha.select_shape(
            SelectedRegions1, 'inner_width', 'and', 120, 300)
        SelectedRegions3 = ha.select_shape(
            SelectedRegions2, 'rectangularity', 'and', 0.9, 1)
        Row, Column, Phi, Length = ha.smallest_rectangle1(SelectedRegions3)
        img_path = Path(img_path)
        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        for i in range(len(Row)):
            try:
                y1 = Row[i]
                x1 = Column[i]
                y2 = Phi[i]
                x2 = Length[i]
                crop_img = img[max(0, y1 - edge):min(h, y2 + edge),
                               max(0, x1 - edge):min(w, x2 + edge)].copy()
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

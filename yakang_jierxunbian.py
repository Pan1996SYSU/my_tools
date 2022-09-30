import os.path
import traceback
from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read

input_path = r"D:\桌面\20220928-OK"
output_path = r"D:\桌面\img"
output_path = Path(output_path)
img_path_list = glob_extensions(input_path)

edge = 0
num = len(img_path_list)
for j, img_path in enumerate(img_path_list):
    if j % 10 == 0:
        print(f'{j / num * 100}%')
    try:
        Image = ha.read_image(img_path)
        Red, Green, Blue = ha.decompose3(Image)
        Regions = ha.threshold(Red, 129, 255)
        RegionComplement = ha.complement(Regions)
        ConnectedRegions = ha.connection(RegionComplement)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'area', 'and', 500000, 2000000)
        Row, Column, Phi, Length = ha.smallest_rectangle1(SelectedRegions)
        if len(Row) != 2:
            print(img_path)
            continue
        img_path = Path(img_path)
        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        if Row[0] < Row[1]:
            y1 = Row[0]
            x1 = Column[0]
            y2 = Phi[0]
            x2 = Length[0]
        else:
            y1 = Row[1]
            x1 = Column[1]
            y2 = Phi[1]
            x2 = Length[1]

        crop_img = img[max(0, y2 - 100 + edge):min(h, y2 + 289 - edge),
                       max(0, x1 - 80 + edge):min(w, x1 + 610 - edge)].copy()
        img_output_path = Path(output_path, img_path.relative_to(input_path))
        if not os.path.exists(img_output_path.parent):
            os.makedirs(img_output_path.parent)
        img_name = os.path.basename(img_output_path).split('.')[0]
        img_suffix = os.path.basename(img_output_path).split('.')[-1]
        cv2.imencode(f'.{img_suffix}', crop_img)[1].tofile(
            f'{img_output_path.parent}/{img_name}.{img_suffix}')
    except Exception as e:
        print(e)
        print(traceback.format_exc())

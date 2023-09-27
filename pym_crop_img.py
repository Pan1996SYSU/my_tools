from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r'D:\桌面\20230926'
output_path = r'D:\桌面\img'

padding = 5

img_path_list = glob_extensions(input_path)

n = len(img_path_list)

aa = n//100

for i, img_path in enumerate(img_path_list):
    try:
        if i % aa == 0:
            print(f'{round(float(i/n), 2)*100}%')
        Image = ha.read_image(img_path)
        Regions = ha.threshold(Image, 160, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'height', 'and', 2000, 10000)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)
        sorted_list = sorted(column1 + column2)
        if len(sorted_list) != 4:
            print(img_path)
            continue
        x1 = sorted_list[1]
        x2 = sorted_list[2]
        img = cv2_read_img(img_path)
        result = img[:, x1+padding:x2-padding].copy()
        img_path = Path(img_path)
        output_img_path = Path(output_path, img_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     result)[1].tofile(output_img_path)
    except:
        print(img_path)

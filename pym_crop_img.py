from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r'D:\桌面\20230925'
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
            ConnectedRegions, 'height', 'and', 500, 10000)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)
        x1 = np.array(column1).min()
        x2 = np.array(column2).max()
        img = cv2_read_img(img_path)
        result = img[:, x1+padding:x2-padding].copy()
        img_path = Path(img_path)
        output_img_path = Path(output_path, img_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     result)[1].tofile(output_img_path)
    except:
        print(img_path)

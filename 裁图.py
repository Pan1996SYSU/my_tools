from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r"Z:\2-现场取图\CYS.230732-01-激光清洗机LDP\1-原图\20231017"
output_path = r'Z:\2-现场取图\CYS.230732-01-激光清洗机LDP\1-原图-pwz已处理\20231017'

img_path_list = glob_extensions(input_path)

pad = 5

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        print(f'{round((i+1) / n * 100, 2)}%')
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 127, 255)
        RegionOpening = ha.opening_rectangle1(Regions, 100, 1)
        ConnectedRegions = ha.connection(RegionOpening)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          1500, 99999)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and', 100,
                                           99999)
        row, column, length1, length2 = ha.smallest_rectangle1(
            SelectedRegions1)
        if len(row) < 2 or len(column) < 2 or len(length1) < 2 or len(

                length2) < 2:
            print(path)
            continue

        x1 = round(np.array(column).min())
        x2 = round(np.array(length2).max())
        y1 = round(np.array(length1).min())
        y2 = round(np.array(row).max())

        img = cv2_read_img(path)
        crop_img = img[y1+pad*4:y2-pad, x1+pad*4:x2-pad*6].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

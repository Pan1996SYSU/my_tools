from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r"D:\桌面\ldp未刻痕"
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

pad = 3

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        print(f'{round((i+1) / n * 100, 2)}%')
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 127, 255)
        RegionOpening = ha.opening_rectangle1(Regions, 100, 1)
        ConnectedRegions = ha.connection(RegionOpening)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          800, 99999)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and', 20,
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
        crop_img = img[y1+5*pad:y2-5*pad, x1+15*pad:x2-15*pad].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r'D:\桌面\20230918-1.3间距'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

pad = 3

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        print(f'{(round(i / n, 4)) * 100}%')
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 180, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          800, 99999)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and',
                                           150, 99999)
        row, column, length1, length2 = ha.smallest_rectangle1(
            SelectedRegions1)
        if len(row) < 2 or len(column) < 2 or len(length1) < 2 or len(
                length2) < 2:
            print(path)
            continue

        x1 = round(np.array(column).min() + pad)
        x2 = round(np.array(length2).max() - pad)
        y1 = round(np.array(length1).min() + pad)
        y2 = round(np.array(row).max() - pad)

        img = cv2_read_img(path)
        crop_img = img[y1:y2, x1:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

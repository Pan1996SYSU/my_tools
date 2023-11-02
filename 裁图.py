from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r"Z:\2-现场取图\CYS.230413-分条机增加外观检测ATL-FTJJC-23023\大图-原图\20231102\黑点1"
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(input_path)

pad = 5

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        print(f'{round((i+1) / n * 100, 2)}%')
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 190, 255)
        RegionOpening = ha.opening_rectangle1(Regions, 100, 1)
        ConnectedRegions = ha.connection(RegionOpening)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          4300, 99999)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and',
                                           40, 99999)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions1)

        sorted_list = sorted(row1 + row2)
        sorted_col = sorted(column1 + column2)
        if len(sorted_list) != 4:
            print(path)
            continue
        y1 = sorted_list[1]
        y2 = sorted_list[2]
        x1 = sorted_col[1]
        x2 = sorted_col[2]

        img = cv2_read_img(path)
        crop_img = img[y1 + pad:y2 - pad, x1 + pad*10:x2 - pad*10].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

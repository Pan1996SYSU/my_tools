from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r"D:\桌面\20231011\10-11"
output_path = r'D:\桌面\img\20231011\10-11'

padding = 10

img_path_list = glob_extensions(input_path)

n = len(img_path_list)

aa = n // 100

for i, img_path in enumerate(img_path_list):
    try:
        # if i % aa == 0:
        #     print(f'{round(float(i/n), 2)*100}%')
        Image = ha.read_image(img_path)
        BlackRegions = ha.threshold(Image,  0, 21)
        BlackConnectedRegions = ha.connection(BlackRegions)
        BlackSelectedRegions = ha.select_shape(BlackConnectedRegions, 'column', 'and', 3000, 99999)
        BlackSelectedRegions1 = ha.select_shape(BlackSelectedRegions, 'height', 'and', 6000, 99999)
        b_row1, b_column1, b_row2, b_column2 = ha.smallest_rectangle1(BlackSelectedRegions1)
        if len(b_row1) != 1:
            print(img_path)
            continue
        x2 = b_column1[0]

        Regions = ha.threshold(Image, 180, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          1500, 10000)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and', 100, 99999)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)
        sorted_list = sorted(row1 + row2)
        sorted_col = sorted(column1 + column2)
        if len(sorted_list) != 4:
            print(img_path)
            continue
        y1 = sorted_list[1]
        y2 = sorted_list[2]
        x1 = sorted_col[1]
        # x2 = sorted_col[2]
        img = cv2_read_img(img_path)
        h, w = img.shape[:2]
        result = img[y1+padding:y2-padding, x1+padding:x2-padding].copy()
        img_path = Path(img_path)
        output_img_path = Path(output_path,
                               img_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix, result)[1].tofile(output_img_path)
    except:
        print(img_path)

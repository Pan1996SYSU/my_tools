from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs

input_path = r'D:/桌面/大图'
output_path = r'D:\桌面\aaa'

padding = 10

img_path_list = glob_extensions(input_path)
img_path_list = img_path_list[208:]
for img_path in img_path_list:
    try:
        Image = ha.read_image(img_path)
        ImageMedian = ha.median_image(Image, 'square', 55, 'mirrored')
        Regions = ha.threshold(ImageMedian, 201, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'width', 'and', 1500, 10000)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)

        if not len(row1) == 2:
            print(img_path)
            continue

        img = cv_img_read(img_path)
        h, w = img.shape[:2]

        if row1[0] < column1[1]:
            x1 = round(min(column1[0], column1[1])) - padding
            y1 = round(row2[0]) - padding
            x2 = round(max(column2[0], column1[1])) - padding
            y2 = round(row1[1]) + padding*2
        else:
            x1 = round(min(column1[0], column1[1])) - padding
            y1 = round(row2[1]) - padding
            x2 = round(max(column2[0], column1[1])) - padding
            y2 = round(row1[0]) + padding*2

        res = img[max(0, y1):min(h, y2), max(0, x1):min(w, x2)].copy()
        output_img_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(Path(img_path).suffix, res)[1].tofile(output_img_path)
    except:
        print(img_path)

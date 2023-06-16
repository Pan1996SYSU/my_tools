from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs

# input_path = r'Z:\2-现场取图\CYS.230413-分条机增加外观检测ATL-FTJJC-23023\大图-原图\20230611\新建文件夹'
# output_path = r'Z:\2-现场取图\CYS.230413-分条机增加外观检测ATL-FTJJC-23023\大图-原图\20230611\新建文件夹-pwz已处理'

padding = 10

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    try:
        Image = ha.read_image(img_path)
        ImageMedian = ha.median_image(Image, 'square', 55, 'mirrored')
        Regions = ha.threshold(ImageMedian, 141, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'width', 'and', 1500, 10000)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)

        if len(row1) == 2:
            img = cv_img_read(img_path)
            h, w = img.shape[:2]

            if row1[0] < column1[1]:
                x1 = round(min(column1[0], column1[1]))
                y1 = round(row2[0]) - padding
                x2 = round(max(column2[0], column1[1])) - padding
                y2 = round(row1[1]) + padding
            else:
                x1 = round(min(column1[0], column1[1])) - padding
                y1 = round(row2[1]) - padding
                x2 = round(max(column2[0], column1[1]))
                y2 = round(row1[0]) + padding

            res = img[max(0, y1):min(h, y2), max(0, x1):min(w, x2)].copy()
            output_img_path = Path(
                output_path,
                Path(img_path).relative_to(Path(input_path)))
            make_dirs(output_img_path.parent)
            cv2.imencode(Path(img_path).suffix, res)[1].tofile(output_img_path)
        elif len(row1) == 1:
            img = cv_img_read(img_path)
            h, w = img.shape[:2]

            x1 = round(column1[0]) - padding
            y1 = 0
            x2 = round(column2[0]) + padding
            y2 = h

            res = img[max(0, y1):min(h, y2), max(0, x1):min(w, x2)].copy()
            output_img_path = Path(
                output_path,
                Path(img_path).relative_to(Path(input_path)))
            make_dirs(output_img_path.parent)
            cv2.imencode(Path(img_path).suffix, res)[1].tofile(output_img_path)
        else:
            print(img_path)
    except:
        print(img_path)

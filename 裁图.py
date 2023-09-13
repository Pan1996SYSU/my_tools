from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r'D:\桌面\新建文件夹'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        print(f'{round(i / n, 4) * 100}%')
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 120, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'height', 'and', 3000, 9999)
        row, column, length1, length2 = ha.smallest_rectangle1(SelectedRegions)
        if len(row) != 2 or len(column) != 2 or len(length1) != 2 or len(length2) != 2:
            print(path)
            continue

        if column[0] < column[1]:
            x1 = column[0]
            x2 = length2[1]
        else:
            x1 = column[1]
            x2 = length2[0]

        img = cv2_read_img(path)
        crop_img = img[:, x1:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

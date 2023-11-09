from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r"Z:\2-现场取图\CYS.230725-清驰质子膜\1-原图"
output_path = r'Z:\2-现场取图\CYS.230725-清驰质子膜\1-原图-pwz已处理'

padding = 10

img_path_list = glob_extensions(input_path)

n = len(img_path_list)

img_list = []

for i, img_path in enumerate(img_path_list):
    try:
        if i % 50 == 0:
            print(f'{round(float(i/n), 3)*100}%')
        Image = ha.read_image(img_path)
        BlackRegions = ha.threshold(Image,  141, 255)
        BlackConnectedRegions = ha.connection(BlackRegions)
        BlackSelectedRegions = ha.select_shape(BlackConnectedRegions, 'width', 'and', 600, 99999)
        b_row1, b_column1, b_row2, b_column2 = ha.smallest_rectangle1(BlackSelectedRegions)
        if len(b_row1) != 1:
            print(img_path)
            img_list.append(img_path)
            continue

        img = cv2_read_img(img_path)
        h, w = img.shape[:2]
        parent = Path(img_path).parent.stem
        if '相机1' in parent:
            x1 = b_column2[0]
            x2 = w
        else:
            x1 = 0
            x2 = b_column1[0]

        result = img[:, x1+padding:x2-padding].copy()
        img_path = Path(img_path)
        output_img_path = Path(output_path,
                               img_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix, result)[1].tofile(output_img_path)
    except:
        print(img_path)
        img_list.append(img_path)

print(img_list)
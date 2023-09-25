from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r'Z:\2-现场取图\CYS.230621-雅策瑞凹版涂布\大图原图\20230918\相机1'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

for path in img_path_list:
    try:
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 140, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'height', 'and',
                                          500, 9999)
        row, column, length1, length2 = ha.smallest_rectangle1(SelectedRegions)
        x1 = column[0]
        x2 = length2[0]

        img = cv2_read_img(path)
        h, w = img.shape[:2]
        crop_img = img[:, 0:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

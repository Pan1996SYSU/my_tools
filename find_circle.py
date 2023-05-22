from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs

r = 100

input_path = r"D:\桌面\img\05-其他"
img_path_list = glob_extensions(input_path)
output_path = r'D:\桌面\新建文件夹'

for img_path in img_path_list:
    try:
        Image = ha.read_image(img_path)
        ImageGauss = ha.gauss_filter(Image, 11)
        Regions = ha.threshold(ImageGauss, 180, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'area', 'and', 10000, 900000)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'roundness', 'and', 0.65, 1.0)
        SelectedRegions2 = ha.select_shape(SelectedRegions1, 'height', 'and', 400, 1700)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions2)

        if not Row1 or not Row2 or not Column1 or not Column2:
            print(img_path)
            continue

        y1 = round(Row1[0]) - r
        x1 = round(Column1[0]) - r
        y2 = round(Row2[0]) + r
        x2 = round(Column2[0]) + r

        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        res_img = img[max(0, y1):min(h, y2),
                      max(0, x1):min(w, x2)].copy()
        img_suffix = Path(img_path).suffix
        output = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        make_dirs(Path(output).parent)
        cv2.imencode(img_suffix, res_img)[1].tofile(output)
    except:
        print(img_path)

from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r"Z:\2-现场取图\CYS.230508-隆深涂布机-长城汽车\正反面"
output_path = r'Z:\4-标注任务\CYS.230508-隆深涂布机-长城汽车\正反面裁图'
padding = 5
img_path_list = glob_extensions(img_path)

for i, path in enumerate(img_path_list):
    try:
        Image = ha.read_image(path)
        img = cv2_read_img(path)
        h, w = img.shape[:2]

        Regions = ha.threshold(Image, 120, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and', 50, 9999)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'height', 'and', 800, 9999)
        row, column, length1, length2 = ha.smallest_rectangle1(SelectedRegions1)
        row2 = [length1[0] + row[0]]
        column2 = [length2[0] + column[0]]
        Rectangle = ha.gen_rectangle1([0], column, [h], column2)
        ReducedImage = ha.reduce_domain(Image, Rectangle)
        Regions1 = ha.threshold(ReducedImage, 0, 188)
        ConnectedRegions1 = ha.connection(Regions1)
        SelectedRegions1 = ha.select_shape(ConnectedRegions1, 'area', 'and', 10000000, 99999999)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions1)
        y1 = Row1[0]
        x1 = Column1[0]
        y2 = Row2[0]
        x2 = Column2[0]

        crop_img = img[:, x1:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

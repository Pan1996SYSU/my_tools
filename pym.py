from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

img_path = r'D:\桌面\新建文件夹'
output_path = r'D:\桌面\img'
padding = 3
img_path_list = glob_extensions(img_path)

for path in img_path_list:
    try:
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 140, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and', 500, 9999)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions)
        Rectangle = ha.gen_rectangle1(Row1, Column1, Row2, Column2)
        ReducedImage = ha.reduce_domain(Image, Rectangle)
        Regions1 = ha.threshold(ReducedImage, 0, 140)
        ConnectedRegions1 = ha.connection(Regions1)
        SelectedRegions1 = ha.select_shape(ConnectedRegions1, 'height', 'and', 500, 9999)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions1)
        y1 = Row1[0] + padding
        x1 = Column1[0] + padding
        y2 = Row2[0] - padding
        x2 = Column2[0] - padding

        img = cv2_read_img(path)
        crop_img = img[y1:y2, x1:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)

    except:
        print(path)

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs
from pathlib import Path

img_path = r'Z:\2-现场取图\CYS.230413-分条机增加外观检测ATL-FTJJC-23023\大图-原图\20230904\0904'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

for path in img_path_list:
    try:
        Image = ha.read_image(path)
        Regions = ha.threshold(Image, 40, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'area', 'and', 10000000, 99999999)
        row, column, length1, length2 = ha.smallest_rectangle1(SelectedRegions)
        row2 = [length1[0] + row[0]]
        column2 = [length2[0] + column[0]]
        Rectangle = ha.gen_rectangle1(row, column, row2, column2)
        ReducedImage = ha.reduce_domain(Image, Rectangle)
        Regions1 = ha.threshold(ReducedImage, 63, 113)
        ConnectedRegions1 = ha.connection(Regions1)
        SelectedRegions1 = ha.select_shape(ConnectedRegions1, 'area', 'and', 10000000, 99999999)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions1)
        y1 = Row1[0]
        x1 = Column1[0]
        y2 = Row2[0]
        x2 = Column2[0]

        img = cv_img_read(path)
        crop_img = img[y1:y2, x1:x2].copy()

        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(img_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix, crop_img)[1].tofile(output_img_path)

    except:
        print(path)
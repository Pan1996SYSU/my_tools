import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs
from pathlib import Path

img_path = r'D:\桌面\20230831-2'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(img_path)

for path in img_path_list:
    try:
        Image = ha.read_image(path)
        ImageInvert = ha.invert_image(Image)
        Regions = ha.threshold(ImageInvert, 137, 255)
        ConnectedRegions = ha.connection(Regions)

        SelectedRegions = ha.select_shape(ConnectedRegions, 'area', 'and', 20000000, 40000000)
        Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions)
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
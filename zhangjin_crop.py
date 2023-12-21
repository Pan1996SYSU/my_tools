from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs

input_path = r"C:\Users\Administrator\Desktop\贴胶工位极耳长度"
output_path = r'C:\Users\Administrator\Desktop\img'

img_path_list = glob_extensions(input_path)

n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        Image = ha.read_image(path)
        Image1, Image2, Image3 = ha.decompose3(Image)
        Regions = ha.threshold(Image1, 0, 160)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'width', 'and',
                                          1000, 99999)
        row1, column1, row2, column2 = ha.smallest_rectangle1(SelectedRegions)

        sorted_list = sorted(row1 + row2)
        sorted_col = sorted(column1 + column2)
        img = cv2_read_img(path)
        h, w = img.shape[:2]
        if len(sorted_list) != 4:
            print(path)
            continue
        parent = Path(path).parent.stem
        y1 = sorted_list[1] - 120
        y2 = sorted_list[1] + 240
        x1 = sorted_col[1] - 100
        x2 = sorted_col[1] + 260
        crop_img = img[y1:y2, x1:x2].copy()
        path = Path(path)
        output_img_path = Path(output_path, path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix,
                     crop_img)[1].tofile(output_img_path)
    except:
        print(path)

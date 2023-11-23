from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import glob_extensions, cv2_read_img, make_dirs
from sonic.lib.new_project_manager import ProjectManager

input_path = r"Z:\2-现场取图\CYS231007-宁德LST上料视觉检测\20231122\解压后\光度立体"
output_path = r'Z:\4-标注任务\CYS231007-宁德LST上料视觉检测\20231122'

img_path_list = glob_extensions(input_path)
n = len(img_path_list)
manager = ProjectManager()
manager.update_file_dict('常规2.5D', img_path_list)

padding = 100
max_h = 2600

for i, img_path in enumerate(img_path_list):
    try:
        print(f'{round((i / n * 100), 2)}%')
        stem = Path(img_path).stem
        parent = Path(img_path).parent.stem
        # if parent == '2d':
        #     continue
        if '_L5_' not in stem:
            continue
        Image = ha.read_image(img_path)
        Regions = ha.threshold(Image, 61, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'area', 'and', 4000000, 9999999)
        row1, column1, row2,column2 = ha.smallest_rectangle1(SelectedRegions)
        if len(row1) != 1:
            print(img_path)
            continue

        y1 = row1[0]
        y2 = row2[0]
        x1 = column1[0]
        x2 = column2[0]

        img_raw_path_list = manager.get_raw_img_list('常规2.5D', img_path)
        for img_raw_path in img_raw_path_list:
            try:
                img = cv2_read_img(img_raw_path)
                h, w = img.shape[:2]
                result = img[max(0, y1 - padding):min(h, y2 + padding), max(0, x1 - padding):min(w, x2 + padding)].copy()
                img_raw_path = Path(img_raw_path)
                output_img_path = Path(output_path,
                                       img_raw_path.relative_to(Path(input_path)))
                make_dirs(output_img_path.parent)
                cv2.imencode(output_img_path.suffix, result)[1].tofile(output_img_path)
            except:
                print(img_raw_path)
    except:
        print(img_raw_path)


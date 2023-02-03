import traceback

import halcon as ha
import cv2
from sonic.utils_func import glob_extensions, cv_img_read
from pathlib import Path

input_path = r"Z:\2-现场取图\CYS.221102-绿胶AI增值ATL-2\24-长胶-左-绿胶-极耳\1"
output_path = r"D:\桌面\img"
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    try:
        SearchImage = ha.read_image(img_path)
        Image1, Image2, Image3 = ha.decompose3(SearchImage)
        Regions = ha.threshold(Image2, 147, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'height', 'and', 10, 1000)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'column1', 'and', 0, 1000)
        RegionUnion = ha.union1(SelectedRegions1)
        Rows, Columns = ha.get_region_points(RegionUnion)
        x1 = min(Columns)
        x2 = max(Columns)
        y1 = min(Rows)
        y2 = max(Rows)
        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        img_res = img[max(0, y1 - 100):min(h, y1 + 100), max(0, x1 - 60):min(w, x2 + 60)].copy()
        suffix = Path(img_path).suffix
        output_img_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        cv2.imencode(suffix, img_res)[1].tofile(output_img_path)
    except Exception as e:
        print(e)
        print(img_path)
        print(traceback.print_exc())



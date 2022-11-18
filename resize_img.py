from sonic.utils_func import cv_img_read, glob_extensions, make_dirs
from pathlib import Path
import cv2

h = 15640
w = 7840

input_path = r'Z:\2-现场取图\CYS.211205-华熔双极板检测\华熔双极板-新板NG\20221118-330'
output_path = r'D:\桌面\pth'

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img = cv_img_read(img_path)
    res_img = cv2.resize(img, (w, h))
    output_img_path = Path(output_path, Path(img_path).relative_to(Path(input_path)))
    suffix = output_img_path.suffix
    make_dirs(output_img_path.parent)
    cv2.imencode(suffix, res_img)[1].tofile(output_img_path)
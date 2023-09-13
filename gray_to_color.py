import shutil
from pathlib import Path

import cv2
from sonic.utils_func import cv2_read_img, glob_extensions, extensions, make_dirs

input_path = r"Z:\5-标注数据\CYS.221126外观检测ATL-TAB-22015_BCU\4-单条检测"
output_path = Path(r"D:\桌面\img")

ext = ['.json']
for e in extensions:
    ext.append(e)

file_path_list = glob_extensions(input_path, ext)

for file_path in file_path_list:
    file_path = Path(file_path)
    suffix = file_path.suffix
    if suffix == '.json':
        output_json_path = Path(
            output_path, file_path.relative_to(Path(input_path)))
        make_dirs(output_json_path.parent)
        shutil.copy(file_path, output_json_path)
    else:
        img = cv2_read_img(file_path)
        color_image2 = cv2.applyColorMap(img, cv2.COLORMAP_BONE)
        output_img_path = Path(
            output_path, file_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(suffix, color_image2)[1].tofile(output_img_path)

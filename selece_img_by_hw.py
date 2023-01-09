import shutil

from sonic.utils_func import glob_extensions, cv_img_read, make_dirs
from pathlib import Path
import os

input_path = r"Z:\5-标注数据\CYS.220924-万宝正负极片外观检测"
output_path = r"D:\桌面\img"

img_path_list = glob_extensions(input_path)
for img_path in img_path_list:
    img_path = Path(img_path)
    json_path = img_path.with_suffix('.json')
    img = cv_img_read(img_path)
    h, w = img.shape[:2]
    if h <= 1024 and w <= 1024:
        output_img_path = Path(output_path, img_path.relative_to(input_path))
        output_json_path = output_img_path.with_suffix('.json')
        make_dirs(output_img_path.parent)
        if os.path.exists(json_path):
            with open(json_path, 'rb') as f_i:
                with open(output_json_path, 'wb') as f_o:
                    shutil.copyfileobj(f_i, f_o, 1024 * 1024)
        with open(img_path, 'rb') as f_in:
            with open(output_img_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, 1024 * 1024)
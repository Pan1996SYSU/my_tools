from pathlib import Path

import cv2
import numpy as np
from sonic.utils_func import cv_img_read, glob_extensions, make_dirs

input_path = r"X:\2-现场取图-3D\CYS.230358-柳州瑞浦【装配线】\L6\转接片\3D\8月\20230810\L6转接片3D"
output_path = r"X:\2-现场取图-3D\CYS.230358-柳州瑞浦【装配线】\L6\转接片\3D\8月\20230810\L6转接片3D-已处理"

path_list = glob_extensions(input_path)

for path in path_list:
    try:
        path = Path(path)
        if path.stem[-1] == 'H':
            img = cv_img_read(path)
            img = (img / 100000 * 1000 / 0.32 + 32767)
            img = np.clip(img, 0, 65535).astype(np.uint16)
            img = ((img - 32767) / 5.0 + 32767).astype(np.uint16)
            output_json_path = Path(output_path, path.relative_to(Path(input_path)))
            make_dirs(output_json_path.parent)
            cv2.imencode(output_json_path.suffix, img)[1].tofile(output_json_path)
        else:
            img = cv_img_read(path)
            output_json_path = Path(output_path, path.relative_to(Path(input_path)))
            make_dirs(output_json_path.parent)
            cv2.imencode(output_json_path.suffix, img)[1].tofile(output_json_path)
    except:
        print(path)
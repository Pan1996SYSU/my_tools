import os.path
import traceback

import numpy as np
from sonic.utils_func import cv_img_read, glob_extensions, make_dirs, load_json,save_json
from pathlib import Path
import cv2

h = 1345
w = 2560
padding = 181


input_path = r'D:\桌面\aaa'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    try:
        img_path = Path(img_path)
        json_path = img_path.with_suffix('.json')

        img = cv_img_read(img_path)
        img_h, img_w = img.shape[:2]

        h_scale = float(h/img_h)
        w_scale = float(w/img_w)

        res_img = cv2.resize(img, (w, h))
        img_with_border = cv2.copyMakeBorder(res_img, padding, padding, 0, 0, cv2.BORDER_CONSTANT, value=0)


        output_img_path = Path(output_path, img_path.relative_to(Path(input_path)))
        suffix = output_img_path.suffix
        make_dirs(output_img_path.parent)
        cv2.imencode(suffix, img_with_border)[1].tofile(output_img_path)

        if os.path.exists(json_path):
            js = load_json(json_path)
            js["imageHeight"] = h
            js["imageWidth"] = w
            for i, shape in enumerate(js["shapes"]):
                points = np.array(shape['points'])
                points[:, 0] = points[:, 0] * w_scale
                points[:, 1] = points[:, 1] * w_scale
                points[:, 1] = points[:, 1] + padding
                js["shapes"][i]['points'] = points.tolist()

            output_json_path = output_img_path.with_suffix('.json')
            save_json(output_json_path, js)
    except Exception as e:
        print(e)
        print(traceback.print_exc())
        print(img_path)
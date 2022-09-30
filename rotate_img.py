import copy
import json
import traceback
from glob import glob
from pathlib import Path

import cv2
import numpy as np
from sonic.utils_func import make_dirs


def rotate(input_path, output_path):
    img_list = glob(input_path + '/**', recursive=True)
    for img_path in img_list:
        try:
            if img_path[-3:] == 'jpg' or img_path[-3:] == 'png' or img_path[
                    -3:] == 'bmp' or img_path[-4:] == 'tiff' or img_path[
                        -3:] == 'tif':
                # 旋转图片
                img_path = Path(img_path)
                img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
                rot_img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
                # 保存图片
                output_img_path = Path(
                    output_path, img_path.relative_to(input_path))
                make_dirs(output_img_path.parent)
                output_img_path = output_img_path.with_suffix('.tiff')
                output_json_path = output_img_path.with_suffix('.json')
                cv2.imencode('.tiff', rot_img)[1].tofile(output_img_path)
                # 修改json
                json_path = img_path.with_suffix('.json')
                try:
                    with open(json_path, "r", encoding='utf-8') as f:
                        js = json.load(f)
                    js_res = copy.deepcopy(js)
                    h = js["imageHeight"]
                    w = js["imageWidth"]
                    for i in range(len(js_res["shapes"])):
                        for j in range(len(js_res["shapes"][i]["points"])):
                            js_res["shapes"][i]["points"][j][1] = js["shapes"][
                                i]["points"][j][0]
                            js_res["shapes"][i]["points"][j][
                                0] = h - js["shapes"][i]["points"][j][1]
                    js_res["imageHeight"] = w
                    js_res["imageWidth"] = h
                    with open(output_json_path, 'w', encoding='utf8') as f:
                        json.dump(js_res, f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(e)
                    traceback.print_exc()
        except Exception as e:
            print(e)
            traceback.print_exc()

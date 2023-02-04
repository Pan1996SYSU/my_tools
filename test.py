import copy
import os.path
from pathlib import Path
import numpy as np
from sonic.utils_func import glob_extensions, load_json, cv_img_read

padding = 50

input_path = r'Z:\5-标注数据\CYS.221102-绿胶AI增值ATL\全AI\绿色短胶\绿色短胶2-右极耳-有槽位'
output_path = r"D:\桌面\img"

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img_path = Path(img_path)
    img = cv_img_read(img_path)
    h, w = img.shape[:2]
    json_path = img_path.with_suffix('.json')
    if os.path.exists(json_path):
        json_data = load_json(json_path)
        shapes = json_data['shapes']
        for shape in shapes:
            if shape['label'] == '绿胶':
                points = np.array(shape['points'])
                x_points = points[:, :1]
                y_points = points[:, 1:]

                x_min = x_points.min()
                y_min = y_points.min()
                x_max = x_points.max()
                y_max = y_points.max()

                crop_img = crop_img = img[max(0, int(y_min - padding)):min(h, int(y_max + padding)), max(0, int(x_min - padding)):min(w, int(x_max + padding))].copy()
                js_data = copy.deepcopy(json_data)

                crop_h, crop_w = crop_img.shape[:2]
                js_data["imageHeight"] = crop_h
                js_data["imageWidth"] = crop_w
                for i, shape in enumerate(js_data["shapes"]):
                    points = np.array(shape['points'])
                    points[:, 0] = points[:, 0] - max(0, int(x_min - padding))
                    points[:, 1] = points[:, 1] - max(0, int(y_min - padding))
                    points[points[:, 0] >= crop_w - 1, 0] = crop_w - 2
                    points[points[:, 0] <= 1, 0] = 2
                    points[points[:, 1] >= crop_h - 1, 1] = crop_h - 2
                    points[points[:, 1] <= 1, 1] = 2
                    js_data["shapes"][i]['points'] = points.tolist()



            elif shape['label'] == '绿胶-带极耳':
                points = np.array(shape['points'])
                x_points = points[:, :1]
                y_points = points[:, 1:]

                x_points = points[:, :1]
                y_points = points[:, 1:]

                x_min = x_points.min()
                y_min = y_points.min()
                x_max = w
                y_max = y_points.max()

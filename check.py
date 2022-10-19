from pathlib import Path

import cv2
import pandas as pd
from sonic.utils_func import load_json, save_json, cv_img_read, glob_extensions, make_dirs

from cut_tencent_img import cut_json

df = pd.read_excel('1.xlsx', sheet_name='2D', usecols='a')
mylist = df.values.tolist()
for path in mylist:
    json_path = str(path[0]).replace('5-标注数据', '4-标注任务')
    try:
        json_data = load_json(json_path)
        file_path = Path(json_path).parent
        img_list = glob_extensions(file_path)
        # for shape in json_data["shapes"]:
        #     points = np.array(shape['points'])
        #     min_x = np.min(points[:, 0])
        #     max_x = np.max(points[:, 0])
        #     x1 = int(min_x - 10)
        #     x2 = int(max_x + 10)
        x1 = 1760
        x2 = 6200
        json_res = cut_json(json_data, x1, x2)
        json_rear_path = json_path.split('4-标注任务')[-1]
        output_json_path = fr'D:\桌面\img{json_rear_path}'
        make_dirs(Path(output_json_path).parent)
        save_json(output_json_path, json_res)
        for img_path in img_list:
            img = cv_img_read(img_path)
            h, w = img.shape[:2]
            res_img = img[0:h, 1760:6200].copy()
            img_rear_path = img_path.split('4-标注任务')[-1]
            output_img_path = fr'D:\桌面\img{img_rear_path}'
            suffix = Path(output_img_path).suffix
            make_dirs(Path(output_json_path).parent)
            cv2.imencode(suffix, res_img)[1].tofile(output_img_path)

    except Exception as e:
        print(json_path)

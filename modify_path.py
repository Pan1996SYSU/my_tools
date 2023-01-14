import traceback

from sonic.utils_func import glob_extensions, load_json, save_json
from pathlib import Path

input_path = r'Z:\5-标注数据\CYS.220717-欣旺达-密封钉检测\2-检测模型-灰度图\OK-all'

json_path_list = glob_extensions(input_path, ['.json'])
for json_path in json_path_list:
    try:
        json_data = load_json(json_path)
        imagePath = json_data["imagePath"]
        image_path_list = json_data["image_path_list"]
        if len(image_path_list) == 1:
            newImagePath = Path(imagePath).name
            new_image_path_list = Path(image_path_list[0]).name
            json_data["imagePath"] = newImagePath
            json_data["image_path_list"] = [new_image_path_list]
            save_json(json_path, json_data)
        else:
            print(image_path_list)
            print('-----------------------------------')
    except Exception as e:
        print(e)
        print(traceback.format_tb())
        print(json_path)
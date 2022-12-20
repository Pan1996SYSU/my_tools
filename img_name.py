from sonic.utils_func import glob_extensions, load_json, save_json
from pathlib import Path

input_path = r"Z:\5-标注数据\CYS.220301-密封钉检测-时代上汽\2D-缺陷检测-RGB"
json_path_list = glob_extensions(input_path, ['.json'])

for json_path in json_path_list:
    new_img_path_list = []
    json_data = load_json(json_path)
    imagePath = json_data["imagePath"]
    image_path_list = json_data["image_path_list"]
    new_img_path = str(Path(imagePath).name)
    for img_path in image_path_list:
        new_img_path_list.append(str(Path(img_path).name))
    json_data["imagePath"] = new_img_path
    json_data["image_path_list"] = new_img_path_list
    if new_img_path != imagePath or new_img_path_list != image_path_list:
        save_json(json_path, json_data)

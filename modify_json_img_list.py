from sonic.utils_func import glob_extensions,load_json,save_json
from pathlib import Path

input_path = r"Z:\4-标注任务\CYS.210333-刀片电池3D焊检测\无为3期\20230307-152349_202303月\NG\auto_label"
json_path_list = glob_extensions(input_path, ['.json'])
for json_path in json_path_list:
    try:
        data = load_json(json_path)
        img_path_list = data["image_path_list"]
        if len(img_path_list) == 2:
            if Path(img_path_list[-1]).stem[-1] in ['H', 'h']:
                data["image_path_list"] = img_path_list + [img_path_list[0]]
            else:
                data["image_path_list"] = [img_path_list[-1]] + img_path_list
            data["channels"] = len(data["image_path_list"])
        save_json(json_path, data)
    except:
        print(json_path)

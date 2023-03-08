from sonic.utils_func import glob_extensions,load_json,save_json

input_path = r"Z:\5-标注数据\0-新项目评估\ZH-DXWG-23001中航包胶后的电芯外观检测"
json_path_list = glob_extensions(input_path, ['.json'])
for json_path in json_path_list:
    data = load_json(json_path)
    img_path_list = data["image_path_list"]
    if len(img_path_list) > 5:
        data["image_path_list"] = data["image_path_list"][:5]
        data["channels"] = len(data["image_path_list"])
    save_json(json_path, data)

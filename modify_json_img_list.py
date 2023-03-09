from sonic.utils_func import glob_extensions, load_json, save_json

input_path = r"Z:\5-标注数据\CYS.220901-南京欣旺达包蓝膜检测\2023.03.09"
json_path_list = glob_extensions(input_path, ['.json'])
for json_path in json_path_list:
    try:
        data = load_json(json_path)
        img_path_list = data["image_path_list"]
        if len(img_path_list) > 6:
            # if Path(img_path_list[-1]).stem[-1] in ['H', 'h']:
            #     data["image_path_list"] = img_path_list + [img_path_list[0]]
            # else:
            #     data["image_path_list"] = [img_path_list[-1]] + img_path_list
            data["image_path_list"] = img_path_list[:6]
            data["channels"] = len(data["image_path_list"])
        save_json(json_path, data)
    except:
        print(json_path)

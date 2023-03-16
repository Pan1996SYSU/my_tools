from sonic.utils_func import glob_extensions, load_json, save_json

target_path = r'D:\桌面\img'
json_path_list = glob_extensions(target_path, ['.json'])

for json_path in json_path_list:
    data = load_json(json_path)
    for i in range(len(data['shapes']) - 1, -1, -1):
        shape = data['shapes'][i]
        points = shape['points']
        if len(set([p[1] for p in points])) != 1:
            continue
        data['shapes'].pop(i)
    save_json(json_path, data)

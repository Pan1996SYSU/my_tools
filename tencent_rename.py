import shutil
from pathlib import Path

from sonic.utils_func import glob_extensions

target_img_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）\侧面\问题'
copy_json_path = r'Z:\7-标注数据-归档\CYS.220661-中航裸电芯-侧面'

json_path_dict = {}

json_path_list = glob_extensions(copy_json_path, ['.json'])
for json_path in json_path_list:
    json_name = Path(json_path).stem
    _position = json_name.index('_')
    if _position < 20:
        json_name = json_name
    else:
        json_name = json_name[5:]
    try:
        s_position = json_name.index('_S')
        i = s_position + 1
        while json_name[i] != '_':
            i += 1
        s_end = i
        pre = json_name[:s_position]
        post = json_name[s_end:]
        json_name = pre + post
    except:
        pass
    try:
        c_position = json_name.index('_C')
        c_end = c_position + 4
        i = c_position + 1
        while json_name[i] != '_':
            i += 1
        c_end = i
        pre = json_name[:c_position]
        post = json_name[c_end:]
        json_name = pre + post
    except:
        pass
    json_path_dict[json_name] = json_path

img_path_list = glob_extensions(target_img_path)
for img_path in img_path_list:
    img_name = Path(img_path).stem
    img_name = img_name[5:]
    try:
        s_position = img_name.index('_S')
        i = s_position + 1
        while img_name[i] != '_':
            i += 1
        s_end = i
        pre = img_name[:s_position]
        post = img_name[s_end:]
        img_name = pre + post
    except:
        pass
    try:
        c_position = img_name.index('_C')
        i = c_position + 1
        while img_name[i] != '_':
            i += 1
        c_end = i
        pre = img_name[:c_position]
        post = img_name[c_end:]
        img_name = pre + post
    except:
        pass
    common_name = img_name.split('_L')[0]
    try:
        json_path = json_path_dict[common_name]
    except:
        print('找不到json文件')
        continue
    img_path_parent = Path(img_path).parent
    json_new_name = str(Path(img_path).name).split('_L')[0]
    json_output_path = f'{img_path_parent}/{json_new_name}.json'
    new_file = shutil.copy(json_path, json_output_path)
    print(f'复制成功{new_file}')

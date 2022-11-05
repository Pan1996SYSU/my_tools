import shutil
import traceback
from collections import defaultdict
from glob import iglob
from pathlib import Path
from sonic.utils_func import extensions, glob_extensions

target_img_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）\侧面\问题'
copy_json_path = r'Z:\7-标注数据-归档\CYS.220661-中航裸电芯-侧面'

json_path_dict = {}

json_path_list = glob_extensions(copy_json_path,  ['.json'])
for json_path in json_path_list:
    json_name = Path(json_path).stem
    try:
        s_position = json_name.index('_S')
    except:
        print(f'找不到_S {json_name}')
        continue
    s_end = s_position + 8
    pre = json_name[5:s_position]
    post = json_name[s_end:]
    json_name_without_s = pre + post
    try:
        c_position = json_name_without_s.index('_C')
    except:
        print(f'找不到_C {json_path }')
        continue
    c_end = c_position + 4
    pre = json_name_without_s[:c_position]
    post = json_name_without_s[c_end:]
    json_name_without_s_without_c = pre + post
    json_path_dict[json_name_without_s_without_c] = json_path

img_path_list = glob_extensions(target_img_path)
for img_path in img_path_list:
    img_name = Path(img_path).stem
    try:
        s_position = img_name.index('_S')
    except:
        print(f'找不到_S {img_path}')
        continue
    s_end = s_position + 8
    pre = img_name[5:s_position]
    post = img_name[s_end:]
    img_name_without_s = pre + post
    try:
        c_position = img_name_without_s.index('_C')
    except:
        print(f'找不到_C {img_name_without_s}')
        continue
    c_end = c_position + 4
    pre = img_name_without_s[:c_position]
    post = img_name_without_s[c_end:]
    img_name_without_s_without_c = pre + post
    common_name = img_name_without_s_without_c.split('_L')[0]
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

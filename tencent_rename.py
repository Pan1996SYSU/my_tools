import shutil
import traceback
from collections import defaultdict
from glob import iglob
from pathlib import Path
from sonic.utils_func import extensions

target_img_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）\侧面\20220913-80NG-117OK'
copy_json_path = r'Z:\5-标注数据\归档\CYS.220661-中航裸电芯-侧面'

img_and_json_path_dict = defaultdict(list)

json_path_list = iglob(f'{copy_json_path}/**/*.json', recursive=True)
for json_path in json_path_list:
    json_name = Path(json_path).name
    common_name = json_name.split('.')[0]
    common_name = common_name.split('_')[0]
    common_name = common_name.split('S')[-1]
    img_and_json_path_dict[common_name].append(json_path)

img_path_list = iglob(f'{target_img_path}/**/*', recursive=True)
for img_path in img_path_list:
    img_suffix = Path(img_path).suffix
    if img_suffix in extensions:
        img_name = Path(img_path).name
        common_name = img_name.split('_')[0]
        common_name = common_name.split('S')[-1]
        try:
            json_path = img_and_json_path_dict[common_name]
            if len(json_path) == 0:
                print(f'找不到对应json{img_path}')
            else:
                json_path = json_path[0]
                img_path_parent = Path(img_path).parent
                json_new_name = str(Path(img_path).name).split('_L')[0]
                json_output_path = f'{img_path_parent}/{json_new_name}.json'
                new_file = shutil.copy(json_path, json_output_path)
                print(f'复制成功{new_file}')
        except:
            print(traceback.format_exc())
            print(json_path)

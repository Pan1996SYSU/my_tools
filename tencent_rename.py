import shutil
import traceback
from collections import defaultdict
from glob import iglob
from pathlib import Path

target_img_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）\20221011_传图\大面\20220914_2-39NG-6OK'
copy_json_path = r'Z:\5-标注数据\CYS.220661-中航裸电芯-大面'

img_and_json_path_dict = defaultdict(set)

img_path_list = iglob(f'{target_img_path}/**/*', recursive=True)
for img_path in img_path_list:
    img_name = Path(img_path).name
    common_name = img_name.split('_')[0]
    common_name = common_name.split('S')[-1]
    img_and_json_path_dict[common_name].add(img_path)

json_path_list = iglob(f'{copy_json_path}/**/*.json', recursive=True)
for json_path in json_path_list:
    json_name = Path(json_path).name
    common_name = json_name.split('.')[0]
    common_name = common_name.split('_')[0]
    common_name = common_name.split('S')[-1]
    try:
        img_path_list = img_and_json_path_dict[common_name]
        if len(img_path_list) == 0:
            print(f'找不到对应图片{json_path}')
        else:
            img_first_path = list(img_path_list)[0]
            img_path_parent = Path(img_first_path).parent
            json_new_name = str(Path(img_first_path).name).split('_L')[0]
            json_output_path = f'{img_path_parent}/{json_new_name}.json'
            new_file = shutil.copy(json_path, json_output_path)
            print(f'复制成功{new_file}')
    except:
        print(traceback.format_exc())
        print(json_path)

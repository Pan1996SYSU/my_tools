from collections import defaultdict
from glob import iglob
from pathlib import Path

target_img_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）\20221011_传图\侧面'
copy_json_path = r'Z:\5-标注数据\CYS.220661-中航裸电芯-侧面'

img_and_json_path_dict = defaultdict(set)

img_path_list = iglob(f'{target_img_path}/**/*', recursive=True)
for img_path in img_path_list:
    img_name = Path(img_path).name
    common_name = img_name.split('_')[0]
    img_and_json_path_dict[common_name].add(img_path)

json_path_list = iglob(f'{copy_json_path}/**/*.json', recursive=True)
for json_path in json_path_list:
    json_name = Path(json_path).name
    common_name = json_path.split('.')[0]
    common_name = common_name.split('_')[0]
    img_and_json_path_dict[common_name].add(json_path)

print(123)
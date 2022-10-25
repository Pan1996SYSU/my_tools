import os
from sonic.utils_func import glob_extensions
from pathlib import Path

target_path = r'Z:\7-标注数据-归档\CYS.220661-中航裸电芯-腾讯定制版\20221011_传图'
json_path_list = glob_extensions(target_path, ['.json'])
n = len(json_path_list)

# for i, json_path in enumerate(json_path_list):
#     if i % 20 == 0:
#         print(i / n * 100)
#     os.remove(Path(json_path))
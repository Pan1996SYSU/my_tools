import os
from sonic.utils_func import glob_extensions
from pathlib import Path

target_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯（2合1）'
json_path_list = glob_extensions(target_path, ['.json'])
n = len(json_path_list)

# for i, json_path in enumerate(json_path_list):
#     if i % 20 == 0:
#         print(i / n * 100)
#     os.remove(Path(json_path))
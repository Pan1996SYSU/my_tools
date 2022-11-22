from glob import glob
import os
from pathlib import Path
import shutil
from sonic.utils_func import make_dirs

input_path = r'Z:\Queenie\瑞浦顶盖焊-缺陷检测'
output_path = r'D:\桌面\img'

file_path_list = glob(f'{input_path}/**', recursive=True)
for file_path in file_path_list:
    if os.path.isdir(file_path):
        continue
    final_output_path = Path(output_path, Path(file_path).name)
    shutil.move(file_path, final_output_path)

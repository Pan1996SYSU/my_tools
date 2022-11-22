from glob import glob
import os
from pathlib import Path
import shutil
from sonic.utils_func import make_dirs

input_path = r'Z:\4-标注任务\CYS.220717-欣旺达-密封钉检测-2D\二线\20221119-白班2DNG-标注中'
output_path = r'D:\桌面\img'

file_path_list = glob(f'{input_path}/**', recursive=True)
for file_path in file_path_list:
    if os.path.isdir(file_path):
        continue
    final_output_path = Path(output_path, Path(file_path).name)
    shutil.move(file_path, final_output_path)

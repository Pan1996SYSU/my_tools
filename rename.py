import os.path
from pathlib import Path

from sonic.utils_func import glob_extensions
input_path = r'D:\桌面\新建文件夹(1)'

json_path_list = glob_extensions(input_path, ['.json'])

for i, file_path in enumerate(json_path_list):
    file_path = Path(file_path)
    stem = str(file_path.stem)
    new_stem = stem.split('_L')[0]
    suffix = str(file_path.suffix)
    new_name = f'{new_stem}{suffix}'
    new_path = Path(Path(file_path).parent, Path(new_name))
    os.rename(file_path, new_path)

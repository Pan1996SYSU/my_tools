import shutil
from sonic.utils_func import glob_extensions, extensions, make_dirs
from pathlib import Path


extensions.add('.json')

input_path = r"Z:\5-标注数据\CYS.230118-柳州瑞浦-极耳翻折\极耳褶皱"
output_path = Path(r'D:\桌面\新建文件夹')

file_path_list = glob_extensions(input_path, extensions)

for file_path in file_path_list:
    file_path = Path(file_path)
    file_name = file_path.name
    new_file_path = Path(output_path, file_name)
    make_dirs(new_file_path.parent)
    shutil.copy2(file_path, new_file_path)
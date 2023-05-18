import shutil
from pathlib import Path

from sonic.utils_func import glob_extensions, extensions, make_dirs

input_path = r'Z:\4-标注任务\CYS.211117-新能德电芯外观检测机\电芯本体-已检查'
output_path = Path(r'Z:\5-标注数据\CYS.230110-新能德电芯本体\本体')

extensions.add('.json')

file_path_list = glob_extensions(input_path, extensions)

for file_path in file_path_list:
    file_path = Path(file_path)
    file_name = file_path.name
    category_name = file_path.parent.name
    file_stem = file_path.stem
    num = file_stem.split('_P0')[-1][0]
    if num in ['5', '6']:
        folder_name = 'P05~P06'
    else:
        folder_name = f'P0{num}'
    output = Path(output_path, folder_name, category_name,file_name)
    make_dirs(output.parent)
    shutil.copy(file_path, output)
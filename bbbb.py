from pathlib import Path

from sonic.utils_func import glob_extensions, extensions

input_path = r'Z:\4-标注任务\CYS.211117-新能德电芯外观检测机\电芯本体-已检查'
output_path = r'Z:\5-标注数据\CYS.230110-新能德电芯本体\本体'

extensions = [key for key in extensions.keys()]
extensions.append('.json')

file_path_list = glob_extensions(input_path, extensions)

for file_path in file_path_list:
    file_path = Path(file_path)
    category_name = file_path.parent.name
    file_stem = file_path.stem
    


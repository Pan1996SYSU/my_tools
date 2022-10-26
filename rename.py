import os.path
from glob import glob
from pathlib import Path

pattern = 'P07'
new_pattern = 'P01'
input_path = r'Z:\5-标注数据\CYS.220661-中航裸电芯-大面'

file_path_list = glob(f'{input_path}/**/*', recursive=True)

n = len(file_path_list)
for i, file_path in enumerate(file_path_list):
    if i % 30 == 0:
        print(i / n * 100)
    if os.path.isfile(file_path):
        file_path = Path(file_path)
        if pattern in file_path.name:
            new_name = str(file_path).replace(pattern, new_pattern)
            new_path = Path(Path(file_path).parent, Path(new_name))
            os.rename(file_path, new_path)
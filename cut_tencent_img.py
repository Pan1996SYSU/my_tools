import os
import traceback
from pathlib import Path

input_path = r'Z:\4-标注任务\20220922-中航叠片电芯-大面'
output_path = r'D:\桌面\img'

extensions = [
    '.bmp', '.gif', '.jpeg', '.jpg', '.pbm', '.png', '.tif', '.tiff', '.json'
]


def get_files_from_dir(path):
    if not os.path.exists(path):
        return ''

    file_path_dict = {}
    for root, directories, files in os.walk(path):
        for filename in files:
            s = Path(filename).suffix
            if s in extensions:
                try:
                    name_key = str(filename).split('_C01_P01')[0]
                    filepath = os.path.join(root, filename)
                    file_path_dict[name_key] = filepath
                except Exception as e:
                    print(e)
                    print(traceback.format_exc())
                    print(filename)
    return file_path_dict


a = get_files_from_dir(r'D:\桌面\sth')
print(a)

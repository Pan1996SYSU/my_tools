import os
import traceback
from collections import defaultdict
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import cv_img_read, load_json, save_json, make_dirs

input_path = r'Z:\5-标注数据\20220922-中航叠片电芯-大面'
thread_num = 16

extensions = [
    '.bmp', '.gif', '.jpeg', '.jpg', '.pbm', '.png', '.tif', '.tiff', '.json'
]

padding = 100


def get_files_from_dir(path):
    if not os.path.exists(path):
        return ''

    file_path_dict = defaultdict(list)
    for root, directories, files in os.walk(path):
        for filename in files:
            s = Path(filename).suffix
            filename = str(filename)
            if s in extensions:
                if 'C01_P01' in filename:
                    name_key = str(filename).split('_C01_P01')[0]
                    filepath = os.path.join(root, filename)
                    file_path_dict[name_key].append(filepath)
                else:
                    print('文件名不存在‘C01_P01’')
                    print(filename)
    return file_path_dict

file_dict = get_files_from_dir(input_path)
for file_key in file_dict:
    h1 = 1
    h2 = 2
    h3 = 3
    h4 = 4
    w1 = 1
    w2 = 2
    w3 = 3
    w4 = 4
    file_list = file_dict[file_key]
    if len(file_list) != 4 and len(file_list) != 5:
        print(file_list)
    elif len(file_list) == 4:
        for i, f in enumerate(file_list):
            img = cv_img_read(f)
            if len(img.shape) != 2:
                print(f)
    elif len(file_list) == 5:
        for i, f in enumerate(file_list):
            if i == 0:
                pass
            else:
                img = cv_img_read(f)
                if len(img.shape) != 2:
                    print(f)
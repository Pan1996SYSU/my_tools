import os
from collections import defaultdict
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

input_path = r'Z:\4-标注任务\20220922-中航叠片电芯-大面'
output_path = r'D:\桌面\img'
thread_num = 16

extensions = [
    '.bmp', '.gif', '.jpeg', '.jpg', '.pbm', '.png', '.tif', '.tiff', '.json'
]


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


def crop_img(task):
    file_key = task.get('file_list', None)
    if file_key is None:
        return
    file_list = file_dict[file_key]
    file_len = len(file_list)
    if file_len == 4:
        pass
    elif file_len == 5:
        pass
    else:
        print('file_list长度不为4或5')
        print(file_list)


file_dict = get_files_from_dir(r'D:\桌面\20220921-22-09-21_陈国栋-已标注-c')
num = len(file_dict)
n = max(1, num // 100)
with ThreadPool(processes=thread_num) as pool:
    tasks = [{
        'file_list': file_list,
    } for file_list in file_dict]
    for i, result in enumerate(pool.imap_unordered(crop_img, tasks)):
        if i % n == 0:
            print(i / num * 100)

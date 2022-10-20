import os
from glob import glob

input_path = r'D:\桌面\pth'


def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)  # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            tf = os.path.join(dir_path, file_name)
            del_files(tf)
    print('ok')

if __name__ == '__main__':
    path_list = glob(f'{input_path}/**/侧面1', recursive=True)
    for path in path_list:
        del_files(path)

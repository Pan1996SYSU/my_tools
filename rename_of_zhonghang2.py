from pathlib import Path
from sonic.utils_func import cv_img_read, make_dirs
import cv2
from glob import glob
from natsort import os_sorted

extensions = ['.bmp', '.gif', '.jpeg', '.jpg', '.pbm', '.png', '.tif', '.tiff']

def glob_extensions1(directory: str, ext_names: list = extensions):
    """
    获取文件夹下所有图片路径
    :param directory: 文件夹路径
    :return: 所以图片路径 type-list
    """
    path_list = []
    new_list = []
    if directory:
        path_list += glob(f'{directory}/**/*', recursive=True)
        for ext in ext_names:
            for x in path_list:
                if x.endswith(ext):
                    x = Path(x)
                    if x.parent.name != '无二维码':
                        new_list.append(x)
    return os_sorted(new_list)

def glob_extensions2(directory: str, ext_names: list = extensions):
    """
    获取文件夹下所有图片路径
    :param directory: 文件夹路径
    :return: 所以图片路径 type-list
    """
    path_list = []
    new_list = []
    if directory:
        path_list += glob(f'{directory}/**/*', recursive=True)
        for ext in ext_names:
            for x in path_list:
                if x.endswith(ext):
                    x = Path(x)
                    if x.parent.name == '无二维码':
                        new_list.append(x)
    return os_sorted(new_list)

input_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯-大面\20221121'
output_path = r'D:\桌面\img'

normal_img_path_list = glob_extensions1(input_path)
no_name_img_path_list = glob_extensions2(input_path)

normal_img_path_dict = {}

a = set()

for norm_img_path in normal_img_path_list:
    norm_img_path = Path(norm_img_path)
    img_name = norm_img_path.stem
    img_name_list = str(img_name).split('_')
    pre = ''
    t = ''
    for element in img_name_list:
        if element == '':
            continue
        if len(element) == 20:
            pre = element
        elif len(element) == 14:
            t = element
        elif len(element) == 17:
            t = element[:-3]
    if pre != '' and t != '':
        normal_img_path_dict[t] = pre

n = len(no_name_img_path_list)

for i, n_img_path in enumerate(no_name_img_path_list):
    if i % 30 == 0:
        print(i / n * 100)
    n_img_path = Path(n_img_path)
    img_name = n_img_path.stem
    img_name_list = str(img_name).split('_')
    pre = ''
    t = ''
    c = ''
    p3 = ''
    l2 = ''
    p2 = ''
    g = ''
    m = ''
    s = ''
    post = ''
    for element in img_name_list:
        if element == '':
            continue
        if len(element) == 20:
            pre = element
        elif len(element) == 14:
            t = element
        elif len(element) == 17:
            t = element[:-3]
        elif len(element) == 7:
            s = element
        elif len(element) == 6:
            post = element
        elif len(element) == 3:
            if element[0] == 'C':
                c = element
            elif element[0] == 'P':
                p3 = element
            else:
                print(f'无法匹配元素 {element}')
        elif len(element) == 2:
            if element[0] == 'L':
                l2 = element
            elif element[0] == 'P':
                p2 = element
            elif element[0] == 'G':
                g = element
            elif element[0] == 'M':
                m = element
            else:
                print(f'无法匹配元素 {element}')
        else:
            print(f'无法匹配元素 {element}')
    if pre == '':
        try:
            pre = normal_img_path_dict[t]
        except:
            a.add(t)
            print(f'找不到对应图片{n_img_path}')

    img = cv_img_read(n_img_path)
    img_stem = f'{pre}_{t}_{c}_{p3}_{l2}_{p2}_{g}_{m}_{s}_{post}'
    img_new_stem = str(img_stem).replace('__', '_')
    img_new_stem = str(img_new_stem).replace('___', '_')
    img_new_stem = str(img_new_stem).replace('____', '_')
    if img_new_stem[0] == '_':
        img_new_stem = img_new_stem[1:]
    if img_new_stem[-1] == '_':
        img_new_stem = img_new_stem[:-1]

    suffix = n_img_path.suffix
    output_img_path = Path(
        output_path,
        Path(n_img_path).relative_to(Path(input_path)))

    output_img_path_parent = output_img_path.parent

    final_output_path = Path(f'{output_img_path_parent}/{img_new_stem}{suffix}')
    make_dirs(final_output_path.parent)

    cv2.imencode(suffix, img)[1].tofile(final_output_path)

print(a)
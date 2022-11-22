from pathlib import Path
from sonic.utils_func import cv_img_read, make_dirs, glob_extensions
import cv2

input_path = r'Z:\4-标注任务\CYS.220661-中航裸电芯-大面\20221121'

img_path_list = glob_extensions(input_path)
for img_path in img_path_list:
    img_path = Path(img_path)
    parent_name = img_path.parent.name
    if parent_name == '无二维码':
        continue
    img = cv_img_read(img_path)
    img_name = img_path.stem
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
    img_stem = f'{pre}_{t}_{c}_{p3}_{l2}_{p2}_{g}_{m}_{s}_{post}'
    img_new_stem = str(img_stem).replace('__', '_')
    if img_new_stem[0] == '_':
        img_new_stem = img_new_stem[1:]
    if img_new_stem[-1] == '_':
        img_new_stem = img_new_stem[:-1]
    

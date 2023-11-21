import re
import shutil
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path
import os
from sonic.utils_func import glob_extensions, make_dirs

img_path = r"X:\2-现场取图\CYS.211117-新能德成品外观检测设备\电芯本体\过漏检-10月21号上线后\过检-10月后\未分"
output_path = r'X:\2-现场取图\CYS.211117-新能德成品外观检测设备\电芯本体\过漏检-10月21号上线后\过检-10月后\未分-pwz已处理'

pattern = r'P0(\d)_'

img_path_list = glob_extensions(img_path)
n = len(img_path_list)

for i, path in enumerate(img_path_list):
    try:
        if i % 100 == 0:
            print(f"{round(i/n*100, 2)}%")
        path_stem = Path(path).stem
        date = re.search(r'(\d{8})-', str(Path(path).parent)).group(1)
        if date is None:
            print(123)
        match = re.search(pattern, path_stem)
        x_value = match.group(1)
        parent = Path(path).parent.stem
        output_img_path = f'{output_path}/{date}/P0{x_value}/{parent}/{Path(path).name}'
        if os.path.exists(output_img_path):
            output_img_path = f'{output_path}/{date}/P0{x_value}/{parent}_{i}/{Path(path).name}'
        make_dirs(Path(output_img_path).parent)
        shutil.copy(path, output_img_path)
    except:
        print(path)

# with ThreadPool(processes=16) as pool:
#     tasks = [{
#         'img_path': img_path,
#     } for img_path in img_path_list]
#     for i, result in enumerate(pool.imap_unordered(work, tasks), n):
#         print(i)

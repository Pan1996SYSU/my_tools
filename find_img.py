import os
import shutil

from sonic.utils_func import glob_extensions
from pathlib import Path

basic_path = r"Z:\5-标注数据\CYS.211117-新能德电芯外观检测机\电芯本体\问题图\裁图不正确"
find_path = r"Z:\5-标注数据\CYS.211117-新能德电芯外观检测机\归档\原图"
output_path = Path(r"Z:\5-标注数据\CYS.211117-新能德电芯外观检测机\电芯本体\问题图\pwz已处理")

basic_img_path_list = glob_extensions(basic_path)
find_img_path_list = glob_extensions(find_path)

b_img_path_list = [str(Path(path).stem) for path in basic_img_path_list]

for find_img_path in find_img_path_list:
    if str(Path(find_img_path).stem) in b_img_path_list:
        output_img_path = Path(output_path, Path(find_img_path).name)
        parent = Path(find_img_path).parent
        stem = Path(find_img_path).stem
        name = str(stem)[:-10]
        json_path = f'{str(parent)}/{name}.json'
        json_output_path = Path(Path(output_img_path).parent,Path(json_path).name)
        if os.path.exists(json_path):
            with open(json_path, 'rb') as f_i:
                with open(json_output_path, 'wb') as f_o:
                    shutil.copyfileobj(f_i, f_o, 1024 * 1024)
        with open(find_img_path, 'rb') as f_in:
            with open(output_img_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, 1024 * 1024)
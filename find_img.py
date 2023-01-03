import shutil

from sonic.utils_func import glob_extensions
from pathlib import Path

basic_path = r"X:\2-现场取图-3D\CYS.220717-欣旺达-密封钉检测-2D\一线\2D-无需分类起\20230101-晚班2D\已确认过杀"
find_path = r"X:\2-现场取图-3D\CYS.220717-欣旺达-密封钉检测-2D\一线\2D-无需分类起\20230101-晚班2D\原图\NG"
output_path = Path(r"X:\2-现场取图-3D\CYS.220717-欣旺达-密封钉检测-2D\一线\2D-无需分类起\20230101-晚班2D\pwz已处理")

basic_img_path_list = glob_extensions(basic_path)
find_img_path_list = glob_extensions(find_path)

b_img_path_list = [str(Path(path).stem) for path in basic_img_path_list]

for find_img_path in find_img_path_list:
    if str(Path(find_img_path).stem) in b_img_path_list:
        output_img_path = Path(output_path, Path(find_img_path).name)
        with open(find_img_path, 'rb') as f_in:
            with open(output_img_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, 1024 * 1024)
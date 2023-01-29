from pathlib import Path
from sonic.utils_func import glob_extensions

input_path = r"X:\2-现场取图-3D\CYS.220818-利元亨南京国轩整线-盖板激光焊接-转接片\1线\20230119\铝极\NG"
output_path = r"D:\桌面\img"

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    
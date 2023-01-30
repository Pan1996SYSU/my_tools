from pathlib import Path
from sonic.utils_func import glob_extensions, make_dirs
import shutil

input_path = r"X:\2-现场取图-3D\CYS.220818-利元亨南京国轩整线-盖板激光焊接-转接片\1线\2023-01"

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img_path = Path(img_path)
    img_stem = str(img_path.stem)
    if 'result' in img_stem:
        output_img_path = Path(img_path.parent, '结果', img_path.name)
    else:
        output_img_path = Path(img_path.parent, '原图', img_path.name)
    make_dirs(output_img_path.parent)
    shutil.move(img_path, output_img_path)


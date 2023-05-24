from pathlib import Path

import cv2
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs

input_path = r'D:\桌面\大图-原图-pwz已处理\20230522-大图-2\压缩图'
output_path = r'D:\桌面\20230522-大图-2\压缩图'

img_path_list = glob_extensions(input_path)
for img_path in img_path_list:
    img = cv_img_read(img_path)
    h, w = img.shape[:2]
    res = img[0:h, 70:w - 70]

    output_img_path = Path(
        output_path,
        Path(img_path).relative_to(Path(input_path)))
    make_dirs(output_img_path.parent)
    cv2.imencode(Path(img_path).suffix, res)[1].tofile(output_img_path)

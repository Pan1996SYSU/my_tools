from pathlib import Path

import cv2
import numpy as np
from sonic.utils_func import glob_extensions, cv_img_read, make_dirs

input_path = Path(r"Z:\4-标注任务\CYS.221102-绿胶AI增值ATL\关键点模型\20230325\crop")
img_path_list = glob_extensions(input_path)
output_path = Path(r'Z:\4-标注任务\CYS.221102-绿胶AI增值ATL\关键点模型\20230325\crop-pwz已处理')

for img_path in img_path_list:
    try:
        img = cv_img_read(img_path)
        # 创建锐化卷积核
        kernel_sharpen_1 = np.array(
            [
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, 25, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]
            ])
        # 应用锐化卷积核
        sharpened = cv2.filter2D(img, -1, kernel_sharpen_1)
        suffix = Path(img_path).suffix
        output_img_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(suffix, sharpened)[1].tofile(output_img_path)
    except:
        print(img_path)

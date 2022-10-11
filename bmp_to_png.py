from pathlib import Path

import cv2
import numpy as np
from sonic.utils_func import glob_extensions

input_path = r'D:\桌面\接带'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(input_path)
for img_path in img_path_list:
    img_path = Path(img_path)
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
    if len(img.shape) > 2:
        img = img[:, :, 0]
    img_path = img_path.with_suffix('.png')
    output_img_path = Path(
        output_path,
        Path(img_path).relative_to(Path(input_path)))
    cv2.imencode('.png', img)[1].tofile(output_img_path)

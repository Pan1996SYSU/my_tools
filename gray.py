import cv2
import numpy as np
from sonic.utils_func import glob_extensions

value = 75

input_path = r'D:\桌面\sonic\resource\ikonate_blue'
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img = cv2.imdecode(
        np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    img[:, :, :3][img[:, :, :3] >= 0] = value
    cv2.imencode('.png', img)[1].tofile(img_path)

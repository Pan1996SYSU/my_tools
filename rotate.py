import cv2
from sonic.utils_func import cv_img_read, glob_extensions
import imutils
import numpy as np
from pathlib import Path

input_path = r'D:\桌面\刀片电池\5'
img_path_list = glob_extensions(input_path)
for img_path in img_path_list:
    img_path = Path(img_path)
    img_name = img_path.name
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
    rot = imutils.rotate(img, angle=-1.7)
    cv2.imencode('.tiff', rot)[1].tofile(f'D:\桌面\pth/{img_name}')

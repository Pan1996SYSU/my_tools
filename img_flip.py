import os.path
import numpy as np
from sonic.utils_func import cv_img_read
from pathlib import Path
import cv2
path = r"D:\桌面\2-00FCE430000004C940312967-20220906-102727.png"
path = Path(path)
img = cv_img_read(path)
res = cv2.flip(img, 0)

cv2.imencode('.png', res)[1].tofile(rf"{path.parent}/pth/3D/{os.path.basename(path)}")
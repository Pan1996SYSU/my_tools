from sonic.utils_func import cv_img_read, show_img
import cv2
import numpy as np

cv_img = cv2.imdecode(np.fromfile(r"D:\桌面\5.png", dtype=np.uint8), cv2.IMREAD_COLOR)
show_img(cv_img)
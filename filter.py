from sonic.utils_func import cv_img_read
import cv2
from pathlib import Path

filter_size = (3, 20)
img_path = r"D:\桌面\2-00PCBGDN01L09CC9C0003217-20220916-022204.png"
suffix = Path(img_path).suffix
img = cv_img_read(img_path)
img_res = cv2.blur(img, filter_size)

cv2.imencode(suffix, img_res)[1].tofile(r"D:\桌面\res2-00PCBGDN01L09CC9C0003217-20220916-022204.png")
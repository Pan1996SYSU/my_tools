from pathlib import Path

import cv2
from sonic.utils_func import cv_img_read

input_path = r'Z:\5-标注数据\20220922-中航叠片电芯-大面\20220925-陈国栋-已标注-检查中\S0000076\05366530767145917440_S000076_C01_P01_L0_PL1_G1_M1_20224525100947_1.bmp'
output_path = r'D:\桌面\img'

img = cv_img_read(input_path)
res_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suffix = Path(input_path).suffix
name = Path(input_path).name
cv2.imencode(suffix, res_img)[1].tofile(f'{output_path}/{name}')

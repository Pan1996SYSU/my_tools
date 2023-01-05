import cv2
from sonic.utils_func import cv_img_read,glob_extensions
from pathlib import Path
from PIL import Image, ImageEnhance

input_path = r"Z:\5-标注数据\CYS.220717-欣旺达-密封钉检测\9-彩图-停产-暂停\针孔"
output_path = r"D:\桌面\pth"
img_path_list = glob_extensions(input_path)

n = 0.2

for img_path in img_path_list:
    img_path = Path(img_path)
    suffix = img_path.suffix
    stem = img_path.stem

    for i in range(5, 10, 1):
        img = Image.open(img_path)
        brightness = i * n
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        img = img.convert("L")
        output_img_path = f'{output_path}/{stem}_{i}{suffix}'
        img.save(output_img_path)
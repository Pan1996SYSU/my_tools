from pathlib import Path

from PIL import Image, ImageEnhance
from sonic.utils_func import glob_extensions, load_json, save_json

input_path = r"Z:\5-标注数据\CYS.220717-欣旺达-密封钉检测\9-彩图-停产-暂停\针孔"
output_path = r"D:\桌面\pth"
img_path_list = glob_extensions(input_path)

n = 0.2

for img_path in img_path_list:
    img_path = Path(img_path)
    suffix = img_path.suffix
    stem = img_path.stem
    json_path = img_path.with_suffix('.json')
    json_data = load_json(json_path)

    for i in range(5, 10, 1):
        img = Image.open(img_path)
        brightness = i * n
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        img = img.convert("L")
        output_img_path = f'{output_path}/{stem}_{i}{suffix}'
        output_json_path = Path(output_img_path).with_suffix('.json')
        img.save(output_img_path)
        save_json(output_json_path, json_data)

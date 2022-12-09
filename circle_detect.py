from sonic.utils_func import show_img, cv_img_read, load_json, glob_extensions, extensions
from pathlib import Path
from glob import glob
import numpy as np
from skimage.transform import resize
import cv2

input_path = r"D:\桌面\20221209-091543_密封钉-焊偏_20221208_164500_D_焊偏\NG"

json_path_list = glob_extensions(input_path, [".json"])
file_path_dict = {Path(json_path).stem: [Path(json_path)] for json_path in json_path_list}
for file in glob(f'{input_path}/**/*.*', recursive=True):
    file = Path(file)
    if file.suffix in extensions:
        for key in file_path_dict.keys():
            if key in file.name:
                file_path_dict[key].append(file)

for key in file_path_dict:
    file_path_list = file_path_dict[key]
    if not file_path_list:
        continue
    json_data = load_json(file_path_list[0])
    for shape in json_data["result"]:
        if shape["category_name"] != "焊偏":
            continue
        x, y, w, h = shape["bbox"]
        mask = np.array(shape["mask"], dtype=np.float32)
        mask = resize(mask, (int(h), int(w)), mode='constant', cval=0)
        mask = (mask * 255).astype(np.uint8)
        image = cv2.copyMakeBorder(mask, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=0)
        print(1)
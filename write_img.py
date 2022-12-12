import cv2
from sonic.utils_func import extensions, glob_extensions, load_json, cv_img_read, make_dirs
from glob import glob
from pathlib import Path

input_path = r"D:\桌面\img\20221212-133540_密封钉-焊偏_20221208_163004_D_4-焊偏模型-灰度图"
output_path = r"D:\桌面\pth"

json_path_list = glob_extensions(input_path, [".json"])
file_path_dict = {
    Path(json_path).stem: [Path(json_path)]
    for json_path in json_path_list
}

for file in glob(f'{input_path}/**/*.*', recursive=True):
    file = Path(file)
    if file.suffix in extensions:
        for key in file_path_dict.keys():
            if key in file.name:
                file_path_dict[key].append(file)

for key in file_path_dict:
    file_path_list = file_path_dict[key]
    if not file_path_list or len(file_path_list) == 1:
        continue
    json_data = load_json(file_path_list[0])
    shape = json_data["result"][0]
    value = round(shape["center_offset_value"],2)
    img = cv_img_read(file_path_list[1])
    cv2.putText(img, f'offset_value: {value}', (500, 850), cv2.FONT_ITALIC, 3, (255, 0, 0), 3)
    output_img_path = Path(output_path, Path(file_path_list[1]).relative_to(Path(input_path)))
    make_dirs(output_img_path.parent)
    cv2.imencode('.jpg', img)[1].tofile(output_img_path)

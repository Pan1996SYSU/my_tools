from glob import glob
from pathlib import Path

import cv2
import numpy as np
from skimage.transform import resize
from sonic.utils_func import load_json, glob_extensions, extensions


def has_white_intersection(img, circle):
    height, width = img.shape[:2]
    circle_img = np.zeros((height, width), dtype="uint8")
    x, y, r = circle
    cv2.circle(circle_img, (x, y), r - 150, (255, 255, 255), -1)
    image = cv2.bitwise_and(img, circle_img)

    # 如果存在相交的白色像素，则返回真
    if image.any() or x - r < 0 or x + r > width or y - r < 0 or y + r > height:
        return True
    else:
        return False


input_path = r"D:\桌面\20221209-091543_密封钉-焊偏_20221208_164500_D_焊偏\NG"

padding = 200

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
        image = cv2.copyMakeBorder(
            mask,
            padding,
            padding,
            padding,
            padding,
            cv2.BORDER_CONSTANT,
            value=0)
        circles = cv2.HoughCircles(
            image,
            cv2.HOUGH_GRADIENT,
            1,
            100,
            param1=50,
            param2=30,
            minRadius=200,
            maxRadius=600)
        # 找到最大内接圆
        if circles is not None:
            # 将圆的坐标转换为整数，方便绘制
            circles = np.round(circles[0, :]).astype("int")

            # 再次筛选，排除中心位于白色区域或超出图片范围的圆
            circles = [
                c for c in circles if not has_white_intersection(image, c)
            ]

            # 找到最大内接圆
            if circles:
                max_circle = max(circles, key=lambda x: x[2])

                # 绘制最大内接圆
                cv2.circle(
                    image, (max_circle[0], max_circle[1]), max_circle[2],
                    (255, 255, 255), 4)

        # 显示结果
        cv2.namedWindow('image', 0)
        cv2.imshow("image", image)
        cv2.waitKey(0)

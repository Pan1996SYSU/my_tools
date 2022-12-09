from glob import glob
from pathlib import Path
import cv2
import numpy as np
from skimage.transform import resize
from sonic.utils_func import load_json, glob_extensions, extensions, show_img
import copy
import time


input_path = r"D:\桌面\20221209-160414_密封钉-焊偏_20221208_164500_D_OK"
padding = 300

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
        s = time.time()
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
        ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        c = copy.deepcopy(binary)
        contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        areas = [cv2.contourArea(c) for c in contours]
        # 求出最大的轮廓的索引
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        (x1, y1), radius = cv2.minEnclosingCircle(cnt)
        hull = cv2.convexHull(cnt)
        h, w = binary.shape[:2]
        a = cv2.drawContours(binary, [hull], 0, (255, 255, 255), -1)
        a = cv2.resize(a, (w, h))
        b = cv2.bitwise_not(a)
        result = cv2.bitwise_or(c, b)
        d = cv2.bitwise_not(result)
        kernel = np.ones((10, 10), np.uint8)
        opening = cv2.morphologyEx(d, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        areas = [cv2.contourArea(c) for c in contours]
        # 求出最大的轮廓的索引
        max_index = np.argmax(areas)
        contour = contours[max_index]
        # 求出轮廓的最小外接圆
        (x2, y2), radius = cv2.minEnclosingCircle(contour)
        dis = np.sqrt(np.square(x2-x1) + np.square(y1-y2))
        print(dis, time.time() - s)
        # cv2.namedWindow('result', 0)
        # cv2.imshow('result', image)
        # cv2.waitKey(0)
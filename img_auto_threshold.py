import json
from pathlib import Path

import cv2
import numpy as np
from sonic.utils_func import cv_img_read, glob_extensions


def cv_simplify_polygon(points_list, simplify_level: int = 1) -> np.ndarray:
    """
    :param simplify_level: 简化等级
    :param points_list: list类型，多边形的各个顶点,值越大，简化出来的点越少
    :return:points_list
    """
    polygon_vertex_2d = np.array(points_list, np.float32)
    x, y = polygon_vertex_2d.min(axis=0)
    w, h = polygon_vertex_2d.max(axis=0) - [x, y]
    w2, h2 = 500, 500
    polygon_vertex_2d -= [[x, y]]
    polygon_vertex_2d /= [[w / w2, h / h2]]
    polygon_vertex_2d = polygon_vertex_2d.astype(np.int32)

    img = np.zeros((h2, w2), dtype=np.uint8)

    cv2.fillPoly(img, [polygon_vertex_2d], 255)

    contours, hierarchy = cv2.findContours(img, 1, 2)
    cnt = contours[-1]

    approx = cv2.approxPolyDP(cnt, simplify_level, True)
    approx = approx[:, 0]

    approx = approx.astype(np.float32)
    approx *= [[w / w2, h / h2]]
    approx += [[x, y]]
    approx = approx.astype(np.int32)
    return approx


input_path = r'D:\桌面\漏金属-光箔'

img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img = cv_img_read(img_path)
    blur = cv2.blur(img, (10, 10))
    res = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 325, 0)
    kernel = np.ones((10, 10), np.uint8)
    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(
        opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(contours) == 0:
        continue

    img_path = Path(img_path)
    img_name = img_path.name
    h, w = img.shape[:2]
    json_path = img_path.with_suffix('.json')

    json_data = {
        "version": "2022.11.21.0",
        "flags": {},
        "imagePath": img_name,
        "imageHeight": h,
        "imageWidth": w,
        "image_path_list": [img_name],
        "channels": 1
    }
    shapes_list = []
    for cnt in contours:
        c = np.squeeze(cnt, axis=1)
        try:
            point_list = (cv_simplify_polygon(c, 5)).tolist()
        except:
            point_list = c.tolist()
        shape_dict = {
            "label": "漏金属",
            "group_id": None,
            "shape_type": "polygon",
            "flags": {},
            "mark": "",
            "points": point_list
        }
        shapes_list.append(shape_dict)
    json_data["shapes"] = shapes_list
    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

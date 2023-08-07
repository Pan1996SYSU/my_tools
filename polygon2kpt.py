import numpy as np
from shapely.geometry import Polygon, LineString


def polygon2kpt_vertical(json_data, points_num):
    point_shapes = []
    for i, shape in reversed(list(enumerate(json_data["shapes"]))):
        if shape['shape_type'] not in ['polygon', 'rectangle']:
            continue
        points = shape['points']
        polygon_points = points

        min_x = np.array(points)[:, 0].min()
        max_x = np.array(points)[:, 0].max()
        min_y = np.array(points)[:, 1].min()
        max_y = np.array(points)[:, 1].max()

        # 创建多边形对象
        polygon = Polygon(polygon_points)

        # 计算矩形的宽度
        rect_width = max_x - min_x

        # 计算宽度平均分成6份得到每个间隔
        interval_width = rect_width / (points_num + 1)

        # 生成6条垂直线的坐标
        vertical_lines = []
        for j in range(1, points_num + 1):
            x_coordinate = min_x + interval_width * j
            vertical_lines.append(
                LineString([(x_coordinate, min_y), (x_coordinate, max_y)]))

        # 计算交点
        intersection_points = []
        for line in vertical_lines:
            intersection = line.intersection(polygon)
            if intersection:
                intersection_points.extend(list(intersection.xy))

        # 输出交点坐标
        n = 0
        for k in range(0, len(intersection_points), 2):
            point_top = {
                "mark": "",
                "label": str(n),
                "points": [
                    [
                        np.array(intersection_points[k]).max(),
                        np.array(intersection_points[k+1]).max()
                    ]
                ],
                "group_id": None,
                "shape_type": "point",
                "flags": {}
            }
            n += 1
            point_bottom = {
                "mark": "",
                "label": str(n),
                "points": [
                    [
                        np.array(intersection_points[k]).min(),
                        np.array(intersection_points[k + 1]).min()
                    ]
                ],
                "group_id": None,
                "shape_type": "point",
                "flags": {}
            }
            n += 1
            point_shapes.append(point_top)
            point_shapes.append(point_bottom)
    json_data["shapes"] = point_shapes
    return json_data


if __name__ == '__main__':
    from sonic.utils_func import load_json, save_json

    js = load_json(r"D:\桌面\sth\3f99bf5ade77b9389676d858c5f4b51c.json")
    js_data = polygon2kpt_vertical(js, 6)
    save_json(r"D:\桌面\新建文件夹\3f99bf5ade77b9389676d858c5f4b51c.json", js_data)

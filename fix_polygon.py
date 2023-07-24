from shapely.geometry import Polygon


def check_polygon_intersection(polygon_points):
    polygon = Polygon(polygon_points)
    if not polygon.is_valid:
        polygon = polygon.buffer(0)

    if polygon.is_valid and polygon.area > 0:
        return False  # 多边形没有交叉或区域重叠
    else:
        return True  # 多边形存在交叉或区域重叠


def fix_polygon_intersection(polygon_points):
    polygon = Polygon(polygon_points)
    polygon = polygon.buffer(0)
    fixed_polygon = polygon.convex_hull
    return fixed_polygon.exterior.coords[:-1]


# 示例点集
polygon_points = [
    (0, 0), (0, 4), (4, 4), (4, 1), (1, 1), (1, 2), (3, 2), (3, 0)
]

# 检测多边形是否存在交叉或区域重叠
if check_polygon_intersection(polygon_points):
    print("多边形存在交叉或区域重叠")
else:
    print("多边形没有交叉或区域重叠")

# 修改多边形为不交叉且区域不重叠
fixed_polygon_points = fix_polygon_intersection(polygon_points)
print("修复后的多边形点集：", fixed_polygon_points)

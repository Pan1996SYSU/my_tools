from datetime import datetime
from pathlib import Path

import cv2
from sonic.utils_func import cv_img_read, glob_extensions, make_dirs


def rotate_image(image, angle):
    # 获取图像的尺寸
    height, width = image.shape[:2]

    # 获取旋转的中心点
    center = (width // 2, height // 2)

    # 计算旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

    # 计算旋转后的尺寸
    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_width = int(height * abs_sin + width * abs_cos)
    new_height = int(height * abs_cos + width * abs_sin)

    # 更新旋转矩阵中心点
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]

    # 应用旋转矩阵到图像
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (new_width, new_height), borderValue=(0, 0, 0))

    return rotated_image


input_path = r'Z:\4-标注任务\CYS.220714-包装机绕胶检测\新建文件'
img_path_list = glob_extensions(input_path)
output_path_45 = r'D:\桌面\新建文件夹\逆时针45'
output_path_minus_45 = r'D:\桌面\新建文件夹\顺时针45'

for img_path in img_path_list:
    img_path = Path(img_path)
    img_suffix = img_path.suffix
    image = cv_img_read(img_path)
    rotated_image_45 = rotate_image(image, 45)
    rotated_image_minus_45 = rotate_image(image, -45)

    output_45_stem = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
    output_45_name = f'{output_45_stem}{img_suffix}'
    output_45 = Path(
        output_path_45,
        Path(img_path).relative_to(Path(input_path)))
    output_45 = Path(output_45.parent, output_45_name)
    make_dirs(Path(output_45).parent)
    cv2.imencode(img_suffix, rotated_image_45)[1].tofile(output_45)

    output_45_minus_stem = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
    output_45_minus_name = f'{output_45_minus_stem}{img_suffix}'
    output_minus_45 = Path(
        output_path_minus_45,
        Path(img_path).relative_to(Path(input_path)))
    output_minus_45 = Path(output_minus_45.parent, output_45_minus_name)
    make_dirs(Path(output_minus_45).parent)
    cv2.imencode(img_suffix, rotated_image_minus_45)[1].tofile(output_minus_45)

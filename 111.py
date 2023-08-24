from pathlib import Path

import cv2
from sonic.utils_func import cv_img_read, glob_extensions, make_dirs


input_path = r"Z:\2-现场取图\CYS.230621-雅策瑞凹版涂布\大图原图\20230823\1 (K34129950)"
output_path = r"Z:\2-现场取图\CYS.230621-雅策瑞凹版涂布\大图原图\20230823\1 (K34129950)-pwz已处理"
# 读取图片
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    try:
        image = cv_img_read(img_path)
        img_path = Path(img_path)

        # 将图片转换为灰度图像
        gray = image

        img_h, img_w = image.shape[:2]

        # 使用二值化方法将白条设置为白色，其他部分设置为黑色
        _, thresholded = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

        # 查找轮廓
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 找到面积最大的轮廓
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour

        # 计算无旋转矩形的 x, y, w, h
        x, y, w, h = cv2.boundingRect(max_contour)

        result = image[0:img_h, 0:x+w].copy()
        output_img_path = Path(output_path, img_path.relative_to(Path(input_path)))
        make_dirs(output_img_path.parent)
        cv2.imencode(output_img_path.suffix, result)[1].tofile(output_img_path)
    except Exception as e:
        print(e)
        print(img_path)
        print('-'*20)


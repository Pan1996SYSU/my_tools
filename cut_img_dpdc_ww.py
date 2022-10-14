from pathlib import Path
from dpdc_parameters import line_5, line_6, line_7, line_8, line_9
import cv2
from sonic.utils_func import glob_extensions, cv_img_read, show_img, make_dirs
'''
行列式负方向
600*800
右上电池x1，y1（940, 10） x2，y2（1740， 610）
左下电池x1，y1（200, 575） x2，y2（1000， 1175）

行列式正方向
600*800
左上电池x1，y1（110, 30） x2，y2（910， 630）
右下电池x1，y1（875, 625） x2，y2（1675， 1225）
'''

input_path = r'D:\桌面\20220930-NG图'
output_path = r'D:\桌面\img'
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img_path = Path(img_path)
    suffix = img_path.suffix
    img = cv_img_read(img_path)
    ret, binary_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    target_index = []
    for i, cnt in enumerate(contours):
        cnt_area = cv2.contourArea(cnt)
        if 900000 <= cnt_area <= 2000000:
            target_index.append(i)

    for index in target_index:
        x, y, w, h = cv2.boundingRect(contours[index])
        rect = cv2.minAreaRect(contours[index])
        crop_img = img[y:y + h, x:x + w].copy()
        output_img_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        output_img_path_parent = output_img_path.parent
        make_dirs(output_img_path_parent)
        output_img_path_all_name = output_img_path.name
        output_img_path_name = output_img_path_all_name.split('.')[0]
        cv2.imencode(suffix, crop_img)[1].tofile(
            f'{output_img_path_parent}/{output_img_path_name}_{index}{suffix}')

        # if h >= 300:
        #     left_mean = crop_img[150:300, 0:w // 2].mean()
        #     right_mean = crop_img[150:300, w // 2:w].mean()
        #     if right_mean < left_mean:
        #         # 为行列式正方向
        #         x1_up = 110
        #         y1_up = 30
        #         x2_up = 910
        #         y2_up = 630
        #         x1_down = 875
        #         y1_down = 625
        #         x2_down = 1675
        #         y2_down = 1225
        #         w_max = x2_down
        #         h_max = y2_down
        #     else:
        #         # 为行列式负方向
        #         x1_up = 940
        #         y1_up = 10
        #         x2_up = 1740
        #         y2_up = 610
        #         x1_down = 200
        #         y1_down = 575
        #         x2_down = 1000
        #         y2_down = 1175
        #         w_max = x2_up
        #         h_max = y2_down
        #     h_crop, w_crop = crop_img.shape[:2]
        # if w_crop >= w_max and h_crop >= h_max:
        #     crop_up_img = crop_img[y1_up:y2_up, x1_up:x2_up].copy()
        #     crop_down_img = crop_img[y1_down:y2_down, x1_down:x2_down].copy()
        #     output_img_path = Path(
        #         output_path,
        #         Path(img_path).relative_to(Path(input_path)))
        #     output_img_path_parent = output_img_path.parent
        #     make_dirs(output_img_path_parent)
        #     output_img_path_all_name = output_img_path.name
        #     output_img_path_name = output_img_path_all_name.split('.')[0]
        #
        #     cv2.imencode(suffix, crop_up_img)[1].tofile(
        #         f'{output_img_path_parent}/{output_img_path_name}_{index}_A{suffix}')
        #     cv2.imencode(suffix, crop_down_img)[1].tofile(
        #         f'{output_img_path_parent}/{output_img_path_name}_{index}_B{suffix}')

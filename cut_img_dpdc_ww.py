from pathlib import Path

import cv2
from sonic.utils_func import glob_extensions, cv_img_read, show_img
'''
600*800
右上电池x1，y1（940, 10） x2，y2（1740， 610）
左下电池x1，y1（200, 575） x2，y2（1000， 1175）
'''

input_path = r'D:\桌面\无为-2D-虚焊'
output_path = r'D:\桌面\img'
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img_path = Path(img_path)
    suffix = img_path.suffix
    img = cv_img_read(img_path)
    ret, binary_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    binary_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, (25, 25))
    contours, hierarchy = cv2.findContours(
        binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    target_index = []
    for i, cnt in enumerate(contours):
        cnt_area = cv2.contourArea(cnt)
        if 1000000 <= cnt_area <= 2000000:
            target_index.append(i)

    for index in target_index:
        x, y, w, h = cv2.boundingRect(contours[index])
        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 10)
        rect = cv2.minAreaRect(contours[index])
        crop_img = img[y:y + h, x:x + w].copy()
        # if h >= 300:
        #     left_mean = crop_img[150:300, 0:w // 2].mean()
        #     right_mean = crop_img[150:300, w // 2:w].mean()
        #     if right_mean < left_mean:
        #         crop_img = cv2.flip(crop_img, 1)
        #     h_crop, w_crop = crop_img.shape[:2]
        # if w_crop >= 1740 and h_crop >= 1175:
        #     crop_up_img = crop_img[10:610, 940:1740].copy()
        #     crop_down_img = crop_img[575:1175, 200:1000].copy()
        #     output_img_path = Path(
        #         output_path,
        #         Path(img_path).relative_to(Path(input_path)))
        #     output_img_path_parent = output_img_path.parent
        #     output_img_path_all_name = output_img_path.name
        #     output_img_path_name = output_img_path_all_name.split('.')[0]
        #
        #     cv2.imencode(suffix, crop_up_img)[1].tofile(
        #         f'{output_img_path_parent}/{output_img_path_name}_{index}_A{suffix}')
        #     cv2.imencode(suffix, crop_down_img)[1].tofile(
        #         f'{output_img_path_parent}/{output_img_path_name}_{index}_B{suffix}')

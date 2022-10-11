from pathlib import Path

import cv2
from sonic.utils_func import glob_extensions, cv_img_read
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
    ret, binary_img = cv2.threshold(img, 88, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    target_index = []
    for i, cnt in enumerate(contours):
        cnt_area = cv2.contourArea(cnt)
        if 1000000 <= cnt_area <= 1500000:
            target_index.append(i)
    if len(target_index) != 0:
        x, y, w, h = cv2.boundingRect(contours[target_index[0]])
        test_img = img[y:y + h, x:x + w].copy()
        test_h, test_w = test_img.shape[:2]

    for index in target_index:
        x, y, w, h = cv2.boundingRect(contours[index])
        crop_img = img[y:y + h, x:x + w].copy()
        h_crop, w_crop = crop_img.shape[:2]
        if w_crop >= 1740 and h_crop >= 1175:
            crop_up_img = crop_img[10:610, 940:1740].copy()
            crop_down_img = crop_img[575:1175, 200:1000].copy()
            output_img_path = Path(
                output_path,
                Path(img_path).relative_to(Path(input_path)))
            output_img_path = output_img_path.rsplit('.', 1)
            cv2.imencode(
                suffix, crop_up_img)[1].tofile(f'{output_img_path}_A{suffix}')
            cv2.imencode(
                suffix,
                crop_down_img)[1].tofile(f'{output_img_path}_B{suffix}')

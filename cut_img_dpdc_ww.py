from pathlib import Path

import cv2
from sonic.utils_func import glob_extensions, cv_img_read
'''
600*800
右上电池x1，y1（940, 10） x2，y2（1740， 610）
左下电池x1，y1（200, 575） x2，y2（1000， 1175）
'''

input_path = r'D:\桌面\img'
img_path_list = glob_extensions(input_path)

for img_path in img_path_list:
    img_path = Path(img_path)
    img = cv_img_read(img_path)
    ret, binary_img = cv2.threshold(img, 88, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    target_index = []
    for i, cnt in enumerate(contours):
        cnt_area = cv2.contourArea(cnt)
        if 1000000 <= cnt_area <= 1500000:
            target_index.append(i)
    for index in target_index:
        x, y, w, h = cv2.boundingRect(contours[index])
        crop_img = img[y:y + h, x:x + w].copy()
        cv2.imencode('.tiff', crop_img)[1].tofile(fr'D:\桌面\{index}.tiff')

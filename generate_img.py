import csv

import cv2
import numpy as np

# 读取csv文件
with open(r"D:\桌面\ANSS5.txt", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

rows = np.array(rows[16384000:16384000*2]).astype(np.float32)

img = rows.reshape((2000, 2048*4, 3))
normal = cv2.normalize(
    img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imencode('.tiff', normal)[1].tofile(r'D:\桌面\ANSS5_pinv2.tiff')

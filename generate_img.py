import csv

import cv2
import numpy as np

# 读取csv文件
with open(r"D:\桌面\ANSS5.txt", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = np.array([row for row in reader])

img = rows.reshape((8000, 8192, 3))
normal = cv2.normalize(
    img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imencode('.tiff', normal)[1].tofile('D:\桌面\ANSS5.tiff')

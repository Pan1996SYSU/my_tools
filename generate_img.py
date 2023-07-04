import csv

import cv2
import numpy as np

with open(r"D:\桌面\ANSS5.txt", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

rows = np.array(rows).astype(np.float32)

img = rows.reshape((8000, 8192, 3))
normal = cv2.normalize(
    img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imencode('.tiff', normal)[1].tofile(r'D:\桌面\ANSS5_pinv2.tiff')

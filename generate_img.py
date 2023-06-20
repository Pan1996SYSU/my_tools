import csv
import numpy as np
from sonic.utils_func import show_img

# 读取csv文件
with open(r"D:\桌面\lstsq2.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

# 将字符串转换为浮点数并除以1048576
data = np.array(rows).astype(np.float32)

# 将数据转换为8位整数
data = (data * 255).astype(np.uint8)
show_img(data)

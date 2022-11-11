import math

import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal
from pylab import mpl

from sklearn.ensemble import IsolationForest

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

file_path = r"D:\桌面\机尾\单面\A面边缘.xls"
excel_data = pd.read_excel(file_path, header=0)

head = list(excel_data.keys())
x = list(excel_data['片数'])

window_length = 200
k = 5

# for i in range(3, 13):
#     y = list(excel_data[head[i]])
#     df = pd.DataFrame({'片数': x, head[i]: y})
#     df.plot('片数', head[i])
#     plt.show()
#     data = list(zip(x, y))
#     predictions = IsolationForest().fit(data).predict(data)
#     y_smooth = scipy.signal.savgol_filter(y, window_length, k)
#     y_res = []
#     for j, flag in enumerate(predictions):
#         if flag == -1:
#             y_res.append(y_smooth[j])
#         else:
#             y_res.append(y[j])
#     df = pd.DataFrame({'片数': x, f'{head[i]}-平滑': y_res})
#     df.plot('片数', f'{head[i]}-平滑')
#     plt.show()

y1 = list(excel_data[head[3]])
y2 = list(excel_data[head[12]])
y = [y2[i] - y1[i] for i in range(len(y1))]
df = pd.DataFrame({'片数': x, '宽': y})
df.plot('片数', '宽')
plt.show()

y1_smooth = scipy.signal.savgol_filter(y1, window_length, k)
data = list(zip(y1, x))
predictions = IsolationForest(contamination=0.1).fit(data).predict(data)
y1_res = []
for j, flag in enumerate(predictions):
    if flag == -1:
        y1_res.append(y1_smooth[j])
    else:
        y1_res.append(y1[j])

y2_smooth = scipy.signal.savgol_filter(y2, window_length, k)
data = list(zip(y2, x))
predictions = IsolationForest(contamination=0.1).fit(data).predict(data)
y2_res = []
for j, flag in enumerate(predictions):
    if flag == -1:
        y2_res.append(y2_smooth[j])
    else:
        y2_res.append(y2[j])
y_smooth = [y2_res[i] - y1_res[i] for i in range(len(y1_res))]
df = pd.DataFrame({'片数': x, '宽-平滑': y_smooth})
df.plot('片数', '宽-平滑')
plt.show()

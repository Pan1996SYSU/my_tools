import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
import scipy.signal

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

file_path = r"D:\桌面\机尾\单面\A面边缘.xls"
excel_data = pd.read_excel(file_path, header=0)

head = list(excel_data.keys())
x = list(excel_data['片数'])

window_length = 500
k = 1

for i in range(3, 13):
    y = list(excel_data[head[i]])
    df = pd.DataFrame({'片数': x, head[i]: y})
    df.plot('片数', head[i])
    plt.show()
    y_smooth = scipy.signal.savgol_filter(y, window_length, k)
    df = pd.DataFrame({'片数': x, f'{head[i]}-平滑': y_smooth})
    df.plot('片数', f'{head[i]}-平滑')
    plt.show()

y1 = list(excel_data[head[3]])
y2 = list(excel_data[head[12]])
y = [y2[i] - y1[i] for i in range(len(y1))]
df = pd.DataFrame({'片数': x, '宽': y})
df.plot('片数', '宽')
plt.show()

y1_smooth = scipy.signal.savgol_filter(y1, window_length, k)
y2_smooth = scipy.signal.savgol_filter(y2, window_length, k)
y_smooth = [y2_smooth[i] - y1_smooth[i] for i in range(len(y1))]
df = pd.DataFrame({'片数': x, '宽-平滑': y_smooth})
df.plot('片数', '宽-平滑')
plt.show()
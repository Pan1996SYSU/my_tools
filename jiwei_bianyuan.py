import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

file_path = r"D:\桌面\机尾\单面\A面边缘.xls"
excel_data = pd.read_excel(file_path, header=0)

head = list(excel_data.keys())
x = list(excel_data['片数'])

for i in range(3, 14):
    y = list(excel_data[head[i]])
    df = pd.DataFrame({'片数': x, head[i]: y})
    df.plot('片数', head[i])
    plt.show()

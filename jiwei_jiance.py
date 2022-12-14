import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

file_path = r"D:\桌面\单面 - 副本\单面 - 副本\OP-12345_201_涂布尺寸检测数据.xls"
excel_data = pd.read_excel(file_path, header=0)

head = list(excel_data.keys())
x = list(excel_data['序号'])

for i in range(5, 13):
    y = list(excel_data[head[i]])

    # index_list = [2475, 2476, 2477, 2478]
    # # 对索引进行反转，使其从后往前删除
    # index_list.reverse()
    # for j in index_list:
    #     if i == 5:
    #         x.pop(j)
    #     y.pop(j)
    df = pd.DataFrame({'序号': x, head[i]: y})
    df.plot('序号', head[i])
    plt.show()

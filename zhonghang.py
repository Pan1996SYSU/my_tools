import pandas as pd

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
import matplotlib.pyplot as plt


file_path = r"D:\桌面\机尾\机尾\A面检测数据2.xls"
excel_data = pd.read_excel(file_path, header=0)

head = list(excel_data.keys())
x = list(excel_data['片数'])

for i in range(5, 14):
    y = list(excel_data[head[i]])

    index_list = [2475, 2476, 2477, 2478]
    index_list.reverse()  # 对索引进行反转，使其从后往前删除
    for j in index_list:
        if i == 5:
            x.pop(j)
        y.pop(j)
    df = pd.DataFrame({'片数': x, head[i]: y})
    df.plot('片数', head[i])
    plt.show()
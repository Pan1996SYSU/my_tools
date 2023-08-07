import matplotlib.pyplot as plt
import numpy as np

# 多边形的点集
points = [(1, 1), (2, 3), (4, 2), (3, 1), (5, 0)]

# 计算曲线拟合多边形
x, y = zip(*points)  # 将点集分离成x和y坐标
p = np.polyfit(x, y, 4)  # 使用3次多项式进行拟合
x_new = np.linspace(min(x), max(x), 100)
y_new = np.polyval(p, x_new)

# 绘制多边形和拟合曲线
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.plot(x, y, 'o', label='多边形')
plt.plot(x_new, y_new, label='拟合曲线')
plt.legend()
plt.show()

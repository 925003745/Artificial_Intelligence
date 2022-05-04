# -*- coding: utf-8 -*-                                                       
# @Time       :   2022/5/2 18:26
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r'D:\pycharm_community\IntelligenceProject\csvFile\out_ttPlus.csv'
f = open(path, 'r', encoding='GB18030')
data = pd.read_csv(f)
print(data)

print("=================================")
x_axis = []
y_axis = []
npArr = np.array(data)

for _ in range(len(npArr)):
    x_axis.append(npArr[_][1])
    y_axis.append(npArr[_][0])

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文

x_axis_data = y_axis
y_axis_data = x_axis

plt.plot(x_axis_data, y_axis_data, 'r', color='#4169E1', alpha=0.8, linewidth=0.75, label='价格')

plt.legend(loc="upper right")

plt.savefig(r'D:\pycharm_community\IntelligenceProject\outFile\ttPlus.png')
plt.show()

print("=================================")

sum_ = data.describe()
print(sum_)

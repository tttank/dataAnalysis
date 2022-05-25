import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')  # 对即将弃用的方法 警告不显示

# 对参数进行设置,不会乱码显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取数据
df = pd.read_excel(r'D:\DataAnalysis\3.pandas\movie_data4.xlsx')


""" 绘制每年上映的电影数量曲线图(1888-2015) """
data = df['年代'].value_counts()
data = data.sort_index()[:-1]
print(data)

# 设置x,y参数
x = data.index
y = data.values

# 生成基本图形
plt.plot(x, y, color='b')

plt.title('每年电影数量', fontsize=20)
plt.ylabel('电影数量', fontsize=18)
plt.xlabel('年代', fontsize=18)

# 每隔10年,显示电影的数量
for a, b in zip(x[::10], y[::10]):
    plt.text(a, b + 10, b, ha='center', va='bottom', fontsize=10)
# 使用 annotate 函数进行注释  xy:注释位置, xytext:注释文字位置
plt.annotate('2012年达到最大值',
             xy=(2012, data[2012]),
             xytext=(2025, 2100),
             arrowprops=dict(facecolor='black', edgecolor='red'))
# 使用 text 在指定位置放入文字
plt.text(1980, 1000, '电影数量开始快速增长')

plt.show()

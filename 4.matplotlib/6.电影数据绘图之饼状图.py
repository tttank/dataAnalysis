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

""" 根据电影长度绘制饼状图 """
"""
pie(x, explode=None, labels=None, colors=None, autopct=None,
    pctdistance=0.6, shadow=False, labeldistance=1.1,
    startangle=None, radius=None)
参数: x 每一块的比例,如果sum(x)>1 会使用sum(x)归一化
labels 每一块饼状图外侧显示的说明文字
explode 每一块离开中心距离
startangle 起始绘制角度,默认从x轴正方向逆时针画起,如果设定=90,则从y轴正方向画起
labeldistance 指定label绘制的位置,相对于半径的比例,如<1则绘制在饼状图内侧
autopct 控制饼状图内百分比设置,可以使用format字符串或者format function
pctdistance 指定autopct的位置刻度
radius 控制饼状图的半径
返回值:如果没有设置autopct,返回(patches,texts)
如果设置autopct,则返回(patches, texts, autotexts)
"""

data = pd.cut(df['时长'], [0, 60, 90, 110, 1000]).value_counts()
print(data)
y = data.values
# y = y / sum(y)  # 每个时间段占总的百分比  写不写这一步都是可以的,自动进行归一化

# 绘图
plt.figure(figsize=(7, 7))  # 设置画布大小

plt.title('电影时长占比', fontsize=15)  # 饼状图标题及字体大小

# patches, l_text:饼图外部字体, p_text:饼图内部字体 设置接受返回值,可以通过返回值修改属性
patches, l_text, p_text = plt.pie(y, labels=data.index, autopct='%.1f %%', colors='bygr',startangle=90)

for i in p_text:   # 设置内部字体属性
    i.set_size(15)
    i.set_color('w')
for i in l_text:  # 设置外部字体属性
    i.set_size(15)
    i.set_color('g')

plt.legend()  # 增加图例
plt.show()

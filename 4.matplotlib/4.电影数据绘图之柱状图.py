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
# print(df[:5])


""" 绘制每个国家或地区的电影数量柱状图 """
data = df['产地'].value_counts()  # 获取产地电影数量信息
print(data)
x = data.index  # 定义x轴参数
y = data.values  # 定义y轴参数

plt.figure(figsize=(10, 6))  # 设置画布大小

# 绘制柱状图 plt.bar()
plt.bar(x, y, color='g')

plt.title('各个国家或地区电影数量', fontsize=20)  # 设置图形的标题

plt.xlabel('国家或地区', fontsize=18)  # x轴的标注名称

plt.ylabel('电影数量', fontsize=18)  # y轴的标注名称

plt.tick_params(labelsize=14)  # 对轴上字体大小重新设置

plt.xticks(rotation=90)  # 将x轴标签字体旋转90度

# 添加文本内容 plt.text()
for a, b in zip(x, y):  # 循环添加全部柱状图
    # text(a,b,c) a:x轴位置, b:y轴位置, c:写的内容
    # ha='center':位置居中显示   va='bottom'/'top':柱状图在数字下面/上面
    plt.text(a, b + 10, b, ha='center', va='bottom', fontsize=10)

# plt.grid()  # 加网格线
plt.show()




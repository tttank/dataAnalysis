import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')  # 对即将弃用的方法 警告不显示

# 对参数进行设置,中文不会乱码显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取数据
df = pd.read_excel(r'D:\DataAnalysis\3.pandas\movie_data4.xlsx')

""" 根据电影评分绘制频率分布直方图 """
# 直⽅图（Histogram）⼜称质量分布图，是⼀种统计报告图，可以被归⼀化以显示“相对”频率。
"""
hist的参数非常多,常用的6个,只有第一个是必选项,后面都是可选项
arr:需要计算直返图的一维数组
bins:直方图的柱数,可选项,默认为 10
normed:是否将得到的直方图向量归一化.默认为0
facecolor:直方图颜色
edgecolor:直方图边框颜色
alpha:透明度

histtype:直方图类型,'bar', 'barstacked', 'step', 'stepfilled'
返回值: n:直方图向量,是否归一化由参数normed设定
bins:返回各个bin的区间范围
patches:返回每个bin里面包含的数据,是一个list
"""

plt.figure(figsize=(10, 6))  # 设置画布大小
plt.hist(df['评分'], bins=20, edgecolor='k', alpha=0.5)

plt.show()

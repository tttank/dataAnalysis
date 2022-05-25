import numpy as np
import pandas as pd

"""
GroupBy技术:实现数据的分组和分组运算,作用类似于数据透视表
"""
df = pd.read_excel('movie_data3.xlsx')

# 按电影的产地进行分组
group = df.groupby(df['产地'])
print(type(group))  # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# 计算分组后的各个统计量
print(group.mean())
print(group.sum())

# 计算每年的平均 评分
print(df['评分'].groupby(df['年代']).mean())

# 只会对数值变量进行分组运算
df['年代'] = df['年代'].astype(str)  # 将年代进行字符串化,剔除年代的聚合运算
print(df.groupby(df['产地']).mean())

# 传入多个分组变量
print(df.groupby([df['产地'], df['年代']]).mean())

# 获得每个地区,每一年电影评分的均值
group = df['评分'].groupby([df['产地'],df['年代']])
means = group.mean()
print(means)

# Series 通过 unstack 方法转化为 DataFrame  会产生缺失值
print(means.unstack().T)
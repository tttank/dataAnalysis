import pandas as pd
import numpy as np

df = pd.read_excel('movie_data2.xlsx')

# 描述性统计
print(df.describe())
# 通过描述性统计,可发现一些异常值
print(df[df['年代'] > 2018])  # 年代超过2018的数据
print(df[df['时长'] > 1000])  # 时长超过1000的数据
# 删除异常数据
df.drop(df[df['年代'] > 2018].index, inplace=True)
df.drop(df[df['时长'] > 1000].index, inplace=True)
print(df[df['年代'] > 2018])  # 再次查询为空
df.index = range(len(df))  # 对行的下标进行重新赋值


# 最值
print(df['投票人数'].max())
print(df['投票人数'].min())

# 均值和中位数
print(df['投票人数'].mean())  # 均值
print(df['投票人数'].median())  # 中位数

#  方差和标准差
print(df['评分'].var())  # 方差
print(df['评分'].std())  # 标准差

# 求和
print(df['投票人数'].sum())

# 相关系数,协方差
print(df[['投票人数', '评分']].corr())  # 相关系数
print(df[['投票人数', '评分']].cov())   # 协方差


# 计数
print(len(df))  # 查看数据长度
# 统计唯一值的统计
print(df['产地'].unique())
print(len(df['产地'].unique()))

# 数据中包含一些重复数据,比如美国和USA, 德国和西德
# 通过数据替换 进行数据合并
df['产地'].replace('USA', '美国', inplace=True)  # 单个替换
df['产地'].replace(['西德', '苏联'], ['德国', '俄罗斯'], inplace=True)  # 列表替换
print(len(df['产地'].unique()))  # 查询产地个数

# 统计年代的唯一值
print(df['年代'].unique())
print(len(df['年代'].unique()))
# 计算每一年电影的数量
print(df['年代'].value_counts()) # 统计年代出现的次数

# 电影产出前5的国家或地区
print(df['产地'].value_counts()[:5])

# 保存数据
df.to_excel('movie_data3.xlsx')

import numpy as np
import pandas as pd

# 读取数据文件excel 或csv
df = pd.read_excel(r'D:\学习\python数据分析\数据分析\pandas\豆瓣电影数据.xlsx')

# 查看前5行
print(df.head())

# 使用 iloc 进行查看操作
print(df.iloc[0])  # 第一行
# print(df.iloc[0:5])  # 前5行 左闭右开的区间
# # 使用 loc 进行查看操作
# print(df.loc[0:5])  # 左闭右闭的区间，6行


# 添加一行
dit = {'名字': '复仇者联盟3', '投票人数': 123456, '类型': '剧情/科幻', '产地': '美国', '上映时间': '2018-05-04 00:00:00', '时长': 142, '年代': 2018, '评分': 8.7, '首映地点': '美国'}
# s = pd.Series(dit)
# s.name = 38738
# print(s)
# df = df.append(s)
# print(df[-5:])


# 删除行
# df = df.drop([38738])
# print(df[-5:])


# 列操作
print(df.columns)  # 取出全部列表头
print(df['名字'][:5])  # 名字列前五行
print(df[['名字', '类型']][:5])  # 两列的前五行


# 增加一列
df['序号'] = range(1, len(df)+1)
print(df[:5])


# 删除列
df = df.drop('序号', axis=1)
print(df[:5])


# 通过 df.loc[[index], [column]] 标签选择数据  index:行下标  column:列名称
print(df.loc[1, '名字'])  # 取 下标为1 的行,列名为 '名字' 的数据
print(df.loc[[1, 3, 5, 7, 9], ['名字', '评分']])


# 条件选择
# 单个条件
print(df[df['产地'] == '美国'][:5])   # 取产地为美国的前五条数据

# 多个条件 and:&
print(df[(df.产地 == '美国') & (df.评分 > 9)])  # 取产地为美国,并且评分大于9的电影

# 多个条件 or:|
print(df[((df.产地 == '美国') | (df.产地 == '中国大陆')) & (df.评分 > 9)])


import numpy as np
import pandas as pd

df = pd.read_excel('movie_data3.xlsx')

# append  即将被弃用,不推荐使用
# df_usa = df[df.产地 == '美国']
# df_china = df[df.产地 == '中国']
# print(df_china.append(df_usa))

"""
merge 横向拼接
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
"""
# 选取6部热门电影
df1 = df.loc[:5]  # 取前六行数据赋值给 df1
print(df1)
df2 = df.loc[:5][['名字', '产地']]  # 取前六行数据的 名字, 产地 赋值给 df2
df2['票房'] = [123344, 23454, 55556, 333, 6666, 444]  # df2添加票房列
print(df2)
# 将df2数据打乱,指的是行
df2 = df2.sample(frac=1)  # index没变
df2.index = range(len(df2))  # 将index重新赋值
print(df2)

# 将 df1 和 df2 合并
print(pd.merge(df1, df2, how='inner', on='名字'))

"""
concat:将多个数据进行批量合并
"""
df1 = df[:10]
df2 = df[100:110]
df3 = df[200:210]
dff = pd.concat([df1, df2, df3])
print(dff)

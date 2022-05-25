import numpy as np
import pandas as pd

"""
离散化处理也可称为分组,区间化
Pandas中使用函数cut():
pd.cut(x,bins,right=True,lables=None,retbins=False,precision=3,include_lowest=False)
x:需要离散化的数组, Series, DataFrame对象
bins:分组的依据
right:右区间默认为闭区间
include_lowest:左区间默认为开区间
lables:定义区间名称,与区间一一对应
"""
# 在实际的数据分析项目中,对有的数据属性,我们往往并不关注数据的绝对值,只关注它所处的区间或者等级

df = pd.read_excel('movie_data3.xlsx')

# 把评分 9分以上定义为A, 7-9分定义为B, 5-7分为C, 3-5分为D, 小于3分为E
print(pd.cut(df['评分'], [0, 3, 5, 7, 9, 10], labels=['E', 'D', 'C', 'B', 'A']))
df['评分等级'] = pd.cut(df['评分'], [0, 3, 5, 7, 9, 10], labels=['E', 'D', 'C', 'B', 'A'])
print(df)

# 根据投票人数来刻画电影的热门
bins = np.percentile(df['投票人数'], [0,20,40,60,80,100])
df['热门程度'] = pd.cut(df['投票人数'], bins, labels=['E', 'D', 'C', 'B', 'A'])
print(df[:5])

# 投票人数很多,评分很低
print(df[(df.热门程度 == 'A') & (df.评分等级 == 'E')])

# 冷门高分电影
print(df[(df.热门程度 == 'E') & (df.评分等级 == 'A')])

# 将处理后的数据进行保存
df.to_excel('movie_data4.xlsx')

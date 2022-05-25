import numpy as np
import pandas as pd

df = pd.read_excel('movie_data3.xlsx')
# print(df[:5])
# 层次化索引 是pandas的一项重要功能,它能使我们在一个轴上拥有多个索引

"""
Series的层次化索引
"""

s = pd.Series(np.arange(1, 10),
              index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(s)
print(s.index)
print(s['a'])
# 切片
print(s['a':'c'])
# 指定一行切片
print(s[:, 1])

# 取具体的值
print(s['c', 3])

# 通过 unstack 方法将Series变成一个DataFrame
print(s.unstack())
print(s.unstack().stack())

"""
DataFrame的层次化索引
"""

data = pd.DataFrame(np.arange(12).reshape(4, 3),
                    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['A', 'A', 'B'], ['Z', 'X', 'C']])
print(data)
print(data['A'])

# 给各个级别设置名称
data.index.names = ['row1', 'row2']
data.columns.names = ['col1', 'col2']
print(data)
# 将 row1 和 row2 位置调换
print(data.swaplevel('row1', 'row2'))

print(df.index)  # RangeIndex(start=0, stop=38162, step=1)

# set_index 可以把列变成索引, reset_index 是把索引变成列
# 把电影中的产地设为外层索引,年代为内层索引
df = df.set_index(['产地', '年代'])
print(df)

# 每一个索引都是一个元祖
print(df.index[0])  # ('美国', 1994)

# 获取所有美国的电影,由于产地信息变成了索引,所以只需使用 loc方法查询
print(df.loc['美国'])
print(df.loc['中国大陆'])
# 这样做的最大好处就是可以简化很多筛选环节

# 调换 产地索引 与 年代索引 的位置
df = df.swaplevel('产地', '年代')
print(df)
# 查询 1994年 电影数据
print(df.loc[1994])

# 取消层次化索引
df = df.reindex()
print(df[:5])

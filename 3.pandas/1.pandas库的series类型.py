import pandas as pd
import numpy as np

# 一维series 可以用一维列表初始化. 索引默认为数字,从0开始
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print('s=', s)
# 指定索引为其他类型
# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(s)

# 索引
print('s.index=', s.index)

# 值
print('s.values=' ,s.values)

# 用索引取值
print('s[0]=', s[0])

# 切片操作
print('s[2:5]', s[2:5])
print('s[::2]', s[::2])

# 索引赋值
s.index.name = '索引'
s.index = list('abcdef')
print('s=', s)
# 取前三行
print('s[:3]=', s[:3])
print("s['a':'c']=", s['a':'c'])

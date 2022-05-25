import pandas as pd
import numpy as np

df = pd.read_excel('movie_data1.xlsx')
# print(df[:5])

# 查看格式
print(df['投票人数'].dtype)
df['投票人数'] = df['投票人数'].astype(float)
print(df['投票人数'].dtype)
print(df[:5])
df['投票人数'] = df['投票人数'].astype(int)
print(df[:5])


# 将年份转为整数格式
# df['年代'] = df['年代'].astype(int)   # 报错 年代不全是符合条件的类型
print(df[df.年代 == '2008\u200e'])

df.loc[14934, '年代'] = 2008

print(df.loc[14934])

df['年代'] = df['年代'].astype(int)

print(df['年代'][:5])


# 将时长转化为整数格式
# df['时长'] = df['时长'].astype(int)   # 报错
print(df[df['时长'] == '8U'])  # 31169
# 删除报错行
df.drop([31169], inplace=True)
# df['时长'] = df['时长'].astype(int)   # 报错 '12J'
print(df[df['时长'] == '12J'])  # 32458
df.drop([32458], inplace=True)

df['时长'] = df['时长'].astype(int)

print(df[:5])


# 按照投票人数进行排序 df.sort_values() 默认升序
print(df.sort_values(by='投票人数'))
# 降序排列
print(df.sort_values(by='投票人数', ascending=False)[:5])

# 按照年代进行排序
print(df.sort_values(by='年代')[:5])

# 多值排序  先按照评分,再按照投票人数
print(df.sort_values(by=['评分', '投票人数'], ascending=False))

# 输出文件
df.to_excel('movie_data2.xlsx')
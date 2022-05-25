import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\学习\python数据分析\数据分析\pandas\豆瓣电影数据.xlsx')
# 添加一个评分缺失的数据
dit = {'名字': '复仇者联盟3', '投票人数': 123456, '类型': '剧情/科幻', '产地': '美国', '上映时间': '2018-05-04 00:00:00', '时长': 142, '年代': 2018, '评分': np.nan, '首映地点': '美国'}
s = pd.Series(dit)
s.name = 38738
print(s)
df = df.append(s)


# 判断缺失值 isnull()
print(df[df['名字'].isnull()])


# 填充缺失值 fillna()
# 数值填充
print(df[df['评分'].isnull()][:10])
df['评分'].fillna(np.mean(df['评分']), inplace=True)
print(df[-1:])

# 字符串填充
df1 = df.fillna('未知电影')  # 全部缺失值填充
print(df1[df1['名字'].isnull()])


# 删除缺失值  df.dropna()  参数:
# how = 'all'  :删除全部为控制的行或者列
# inplace = True  :覆盖之前的数据
# axis = 0   : 选择行或列  默认选择行 删除
print(len(df))
df2 = df.dropna()  # 复制给 df2 变量
print(len(df2))

df.dropna(inplace=True)  # 覆盖原值
print(len(df))


# 处理异常值 在数据集中存在不合理的值,又称离群点
print(df[df.投票人数 < 0])
print(df[df['投票人数'] % 1 != 0])
# 保留正常数据
df = df[df.投票人数>0]
df = df[df['投票人数'] % 1 == 0]
print(df[df.投票人数 < 0])
print(df[df['投票人数'] % 1 != 0])


# 数据保存
df.to_excel('movie_data1.xlsx')
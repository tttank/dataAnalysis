import pandas as pd
import numpy as np

df = pd.read_excel('movie_data3.xlsx')

# 基础形式
pd.options.display.max_rows = 500  # 解除显示限制,可展示500行
pd.options.display.max_columns = 20  # 可展示20列
print(pd.pivot_table(df, index='年代'))  # 默认求平均数

# 使用多个索引  索引为 年代,产地   index =
print(pd.pivot_table(df, index=['年代', '产地']))

# 指定需要统计汇总的数据  只查询 评分  values =
print(pd.pivot_table(df, index=['年代', '产地'], values=['评分']))

# 使用指定函数来统计值  aggfunc =
print(pd.pivot_table(df, index=['年代', '产地'], values='投票人数', aggfunc=np.sum))

# 通过将 投票人数 列和 评分 列进行对应分组, 对 产地 实现数据聚合和总结
print(pd.pivot_table(df, index=['产地'], values=['投票人数', '评分'], aggfunc=[np.sum, np.mean]))

# 非数字 Nan 难以处理,可以使用 fill_value 将其设置为0
print(pd.pivot_table(df, index=['产地'], aggfunc=[np.sum, np.mean], fill_value=0))

# 加入 margins = True 在下方显示总和
print(pd.pivot_table(df, index=['产地'], aggfunc=[np.sum, np.mean], fill_value=0, margins=True))

# 对不同值执行不同函数:可以向aggfunc传递一个字典
print(pd.pivot_table(df, index=['产地'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0))

# 对各个年份 的 投票人数求和, 对评分求均值
print(pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'],
                     aggfunc={'投票人数': np.sum, '评分': np.mean},
                     fill_value=0,margins=True))

# 透视表过滤
table = pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0)
print(type(table))  # <class 'pandas.core.frame.DataFrame'>
print(table[:5])

# 查询 1994年的数据
print(table[table.index == 1994])

# 按照评分排列
print(table.sort_values('评分', ascending=False))   # 降序

# 按照多个索引来进行汇总
print(pd.pivot_table(df, index=['产地','年代'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0))

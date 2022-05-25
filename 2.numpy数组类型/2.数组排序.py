import numpy as np

# 电影名称
mv_name = ['肖申克的救赎', '控方证人', '美丽人生 ', '阿甘正传', '霸王别姬', '泰坦尼克号 ', '辛德勒的名单', '这个杀手不太冷 ', '疯狂动物城', '海豚湾']
# 评分人数
mv_num = np.array([692795, 42995, 327855, 580897, 478523, 157074, 306904, 662552, 284652, 159302])
# 评分
mv_score = np.array([9.6, 9.5, 9.5, 9.4, 9.4, 9.4, 9.4, 9.4, 9.3, 9.3])
# 电影时长（分钟）
mv_length = np.array([142, 116, 116, 142, 171, 194, 195, 133, 109, 92])

# sort函数， 不会改变原数组顺序
print(np.sort(mv_num))

# argsort函数 返回从小到大的排列在数组中的索引位置
order = np.argsort(mv_num)
print(order)  # [1 5 9 8 6 2 4 3 7 0]

# 获取评分人数最少的索引
index = order[0]
print(mv_name[index])  # 控方证人

# 求和
print(np.sum(mv_num))
print(mv_num.sum())

# 最大值
print(np.max(mv_length))
print(mv_length.max())

# 最小值
print(np.min(mv_score))
print(mv_score.min())

# 均值
print(np.mean(mv_length))
print(mv_length.mean())

# 标准差

print(np.std(mv_length))
print(mv_length.std())

# 相关系数矩阵
print(np.cov(mv_score, mv_length))

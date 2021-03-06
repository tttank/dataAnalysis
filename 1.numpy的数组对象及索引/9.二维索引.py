import numpy as np

a = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55]])
print(a)
# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]

# 返回的是一条对角线上的5个值
print(a[(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)])  # [ 0 11 22 33 44 55]

# 返回的是最后三行的 第1,3,5列
print(a[-3:, ::2])  # 用切片
print(a[-3:, [0, 2, 4]])  # 用索引

# 使用mask进行索引
mask = np.array([1, 0, 1, 0, 0, 1], dtype=bool)
print(a[mask, 2])  # [ 2 22 52]

# 与切片不同，花式索引返回的是原对象的一个复制 而不是引用

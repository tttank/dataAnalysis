import numpy as np

# 数组形状
a = np.arange(6)
print(a)  # [0 1 2 3 4 5]

a.shape = 2, 3
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.shape)  # (2, 3)

# reshape 方法，不会修改原来数组的值，而是返回一个新的数组
a = np.arange(6)
print(a.reshape(2, 3))
# [[0 1 2]
#  [3 4 5]]
print(a)  # [0 1 2 3 4 5]

# 转置
a = a.reshape(2,3)
print(a)
# [[0 1 2]
#  [3 4 5]]
print(a.T)
# [[0 3]
#  [1 4]
#  [2 5]]
print(a.transpose())
# [[0 3]
#  [1 4]
#  [2 5]]
print(a)






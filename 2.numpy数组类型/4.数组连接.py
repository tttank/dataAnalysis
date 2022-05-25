import numpy as np

# 数组连接，将不同数组按照一定顺序连接起来
x = np.array([[0, 1, 2], [10, 11, 12]])
y = np.array([[50, 51, 52], [60, 61, 62]])

# 查看数组形状
print(x.shape)  # (2, 3)
print(y.shape)  # (2, 3)

# 默认沿着第一维进行连接
z = np.concatenate((x, y))
print(z)
# [[ 0  1  2]
#  [10 11 12]
#  [50 51 52]
#  [60 61 62]]

# 沿着第二维进行连接
z = np.concatenate((x, y), axis=1)
print(z)
# [[ 0  1  2 50 51 52]
#  [10 11 12 60 61 62]]

# 使用 array 沿着三维 进行连接
z = np.array((x, y))
print(z)
# [[[ 0  1  2]
#   [10 11 12]]
#
#  [[50 51 52]
#   [60 61 62]]]
print('~'*50)

#  事实上，Numpy提供了分别对应这三种情况的函数
# 沿着一维 进行连接： vstack     一维：以列连接
print(np.vstack((x, y)))

# 沿着二维 进行连接： hstack     二维：以行连接
print(np.hstack((x, y)))

# 沿着三维 进行连接： dstack     三维：以整个数组进行连接
print(np.dstack((x, y)))
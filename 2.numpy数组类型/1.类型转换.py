#  数据类型转换
import numpy as np

# 使用 dtype 指定数据类型
a = np.array([1, 2.5, -3], dtype=float)
print(a)  # [ 1.   2.5 -3. ]

# asarray 函数
b = np.array([1, 2, 3])
b = np.asarray(b, dtype=float)
print(b)  # [1. 2. 3.]

# astype 方法 返回 一个新的数组
a = np.array([1, 2, 3])
b = a.astype(float)
print(b)  # [1. 2. 3.]
b[0] = 10
print(b)  # [10.  2.  3.]
print(a)  # [1 2 3]

"""
花式索引
"""
# 切片只能支持连续或者登剑阁的切片操作，要想实现任意位置的操作，需要使用花式索引 fancy slicing
import numpy as np

# 一维花式索引
a = np.arange(0, 100, 10)
print(a)  # [ 0 10 20 30 40 50 60 70 80 90]

# 花式索引需要指定索引位置
index = [1, 2, -3]
y = a[index]
print(y)  # [10 20 70]

# 使用布尔数组来花式索引
mask = np.array([0, 2, 2, 0, 0, 1, 0, 0, 1, 0], dtype=bool)
print(mask)  # [False  True  True False False  True False False  True False]
# mask必须是布尔数组 长度必须和 数组长度相等
print(a[mask])  # [10 20 50 80]

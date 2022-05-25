# where 函数会返回所有非零元素的索引
import numpy as np

a = np.array([0, 12, 5, 20])
# 判断数组中的元素是否大于10，返回布尔类型
print(a > 10)  # [False  True False  True]

# 数组中所有大于10 的元素索引位置，返回值是一个元祖
print(np.where(a > 10))  # (array([1, 3], dtype=int64),)

# 直接用数组操作 取出符合条件的元素
print(a[a > 10])  # [12 20]

# 使用where获取符合条件元素索引，利用索引获取元素
print(a[np.where(a > 10)])  # [12 20]


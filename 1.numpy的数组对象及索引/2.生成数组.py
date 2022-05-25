"""
生成数组
"""
import numpy as np

# 从列表产生数组
l = [0, 1, 2, 3]
a = np.array(l)
print(a)  # [0 1 2 3]

# 从列表传入
a = np.array([1, 2, 3, 4])
print(a)  # [1 2 3 4]

# 生成全0数组，默认生成浮点数
a = np.zeros(5)
print(a)  # [0. 0. 0. 0. 0.]

# 生成全1的数组，默认浮点数，加 dtype = int 可修改为整数
a = np.ones(5, dtype=int)
print(a)  # [1 1 1 1 1]
print(type(a))  # <class 'numpy.ndarray'>
for i in a:
    print(i)
a = np.ones(5, dtype=bool)
print(a)  # [ True  True  True  True  True]

# 使用fill方法设为指定值
a = np.array([1, 2, 3, 4])
# 使用整数
a.fill(5)
print(a)  # [5 5 5 5]
# 使用浮点数,默认情况下会向下取整
a.fill(2.6)
print(a)  # [2 2 2 2]
# 修改数据类型
a = a.astype(float)
a.fill(2.5)
print(a)  # [2.5 2.5 2.5 2.5]

# 生成整数序列
a = np.arange(1, 10)  # 左闭右开
print(a)  # [1 2 3 4 5 6 7 8 9]
a = np.arange(1, 10, 2)
print(a)  # [1 3 5 7 9]

# 生成等差数列，默认为浮点数float
a = np.linspace(1, 10, 10)   # 左闭右闭，1-10 都包含在里面,取10个数
print(a)  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

a = np.linspace(1, 10, 21)  # 1-10 都包含，取21个数
print(a)  # [ 1.    1.45  1.9   2.35  2.8   3.25  3.7   4.15  4.6   5.05  5.5   5.95  6.4   6.85  7.3   7.75  8.2   8.65  9.1   9.55 10.  ]

# 生成随机数
a = np.random.rand(10)  # 生成0-1之间的10个随机数
print(a)

a = np.random.randn(10)  # 生成10个符合正态分布的随机数
print(a)

a = np.random.randint(1, 10, 10)  # 生成1-10之间的10个整数
print(a)

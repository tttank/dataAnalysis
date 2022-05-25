import numpy as np

a = np.array([0, 1, 2, 3])

# 索引第一个值
print(a[0])

# 修改第一个元素的值
a[0] = 10
print(a)

a = np.array([11, 12, 13, 14, 15])
print(a)
# 切片支持负索引  索引左闭右开
print(a[1:3])
print(a[1:-2])
print(a[-4:3])

# 省略参数
print(a[-2:])
print(a[::2])


# 假设我们记录一部电影票房
ob = np.array([21000, 21800, 22400, 23450, 25000])
# 计算每天新增的票房
ob2 = ob[1:] - ob[:-1]
print(ob2)

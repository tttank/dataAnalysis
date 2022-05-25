import numpy as np

a = np.random.randn(10)
print(a)
# 查看数组数据类型
print(type(a))

# 查看数组中的数据类型
print(a.dtype)

# 查看形状，会返回一个元祖，每个元素代表这一堆元素的数目
print(a.shape)

# 查看数组中的元素数目有多少个
print(a.size)

# 查看 数组 的维度
print(a.ndim)

import numpy as np

a = [1, 2, 3, 4]
# 想实现a中每个元素+1
print([x + 1 for x in a])  # [2, 3, 4, 5]

b = [2, 3, 4, 5]
# 实现a+b，对应元素相加
print(a + b)  # 得到的是 [1, 2, 3, 4, 2, 3, 4, 5]
print([x + y for (x, y) in zip(a, b)])  # 得到 [3, 5, 7, 9]
# 以上方法的实现都是用到列表生成式，操作麻烦。数据量大时非常耗时

print('~' * 50)  # 分割线

a = np.array([1, 2, 3, 4])
print(a)  # [1 2 3 4]
print(a + 1)  # [2 3 4 5]
print(a * 2)  # [2 4 6 8]
b = np.array([2, 3, 4, 5])
print(a + b)  # [3 5 7 9]

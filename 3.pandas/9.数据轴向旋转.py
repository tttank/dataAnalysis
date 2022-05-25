import numpy as np
import pandas as pd

df = pd.read_excel('movie_data3.xlsx')
data = df[:5]
print(data)

# 使用 .T 使数据的行列进行交换
print(data.T)

# DataFrame也可以使用stack 和 unstack 转化为层次化索引的Series
print(data.stack().unstack())


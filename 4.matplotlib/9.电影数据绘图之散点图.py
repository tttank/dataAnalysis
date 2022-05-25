import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import matplotlib.mlab as mlab
from scipy import stats

warnings.filterwarnings('ignore')  # 对即将弃用的方法 警告不显示

# 对参数进行设置,中文不会乱码显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r'D:\DataAnalysis\3.pandas\movie_data4.xlsx')

x = df['时长'][::100]
y = df['评分'][::100]

plt.figure(figsize=(10, 6))

# 散点图 plt.scatter(x,y)   marker:设置形状
plt.scatter(x, y, color='c', marker='D')

# plt.legend()  # 展示图例

plt.title('电影时长与评分散点图', fontsize=20)

plt.xlabel('时长', fontsize=18)
plt.ylabel('评分', fontsize=18)


plt.show()

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
# print(df[:5])

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)

# 绘制直方图
n, bins, patches = ax1.hist(df['评分'], bins=100, color='m')

ax1.set_ylabel('电影数量', fontsize=15)
ax1.set_xlabel('评分', fontsize=15)
ax1.set_title('频率分布图', fontsize=20)

y = stats.norm.pdf(bins, df['评分'].mean(), df['评分'].std())

ax2 = ax1.twinx()
ax2.plot(bins, y, 'b--')
ax2.set_ylabel('概率分布',fontsize=15)

plt.show()
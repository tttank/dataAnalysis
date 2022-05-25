import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import seaborn as sns

warnings.filterwarnings('ignore')  # 对即将弃用的方法 警告不显示

# 对参数进行设置,中文不会乱码显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取数据
df = pd.read_excel(r'D:\DataAnalysis\3.pandas\movie_data4.xlsx')

data = df[['投票人数','评分','时长']]
# print(data[:5])

# 画各个属性之间的散点图,对角线是分布图
# result = pd.plotting.scatter_matrix(data[::100], diagonal='kde', color='k',
#                                     alpha=0.3, figsize=(10, 10))


# 相关系数矩阵图 时长,投票人数,评分
corr = data.corr()
corr=abs(corr)
# 绘图
fig = plt.figure(figsize=(10, 8))
ax = plt.subplots(figsize=(10, 8))

ax = sns.heatmap(corr, vmax=1, vmin=0, annot=True, annot_kws={'size':13, 'weight':'bold'}, linewidths=0.05)

plt.title('热力图', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


plt.show()

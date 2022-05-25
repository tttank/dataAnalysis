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

# 美国电影评分的箱线图
# data = df[df.产地 == '美国']['评分']
# plt.figure(figsize=(10, 6))
# # 绘制图形
# plt.boxplot(data, whis=2)
# plt.title('美国电影评分', fontsize=20)

# 多组数据箱线图
data1 = df[df.产地 == '中国大陆']['评分']
data2 = df[df.产地 == '日本']['评分']
data3 = df[df.产地 == '中国香港']['评分']
data4 = df[df.产地 == '英国']['评分']
data5 = df[df.产地 == '法国']['评分']

plt.figure(figsize=(12, 8))
plt.boxplot([data1, data2, data3, data4, data5], labels=['中国大陆', '日本', '中国香港', '英国', '法国'],
            whis=2, flierprops={'marker': 'o', 'markerfacecolor': 'r', 'color': 'k'},
            patch_artist=True, boxprops={'color': 'k', 'facecolor': '#9999ff'},
            vert=False)

plt.title('电影评分箱线图', fontsize=20)
# 获取坐标系
ax = plt.gca()
ax.patch.set_facecolor('gray')  # 背景颜色
ax.patch.set_alpha(0.3)  # 背景透明度


plt.show()

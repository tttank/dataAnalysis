import matplotlib.pyplot as plt
import numpy as np

# 在一个图里画多条线  传入多组数据
# t = np.arange(0, 5, 0.2)
# plt.plot(t, t, 'r--',
#          t, t ** 2, 'bs',
#          t, t ** 3, 'g^')
# plt.show()


# 使用关键词改变线条性质:例如 linewidth 可以改变线条宽度, color 可以改变线条颜色
x = np.linspace(-np.pi, np.pi)
y = np.sin(x)
# plt.plot(x, y, linewidth=4.0, color='r')
# plt.show()


"""
使用plt.plot()的返回值来设置线条属性
plot函数返回一个Line2D对象组成的列表,每个对象代表输入的一对组合
== line1,line2为两个Line2D对象
    line1, line2 = plt.plot(x1,y1, x2,y2)
== 返回3个Line2D对象组成的列表
    lines = plt.plot(x1,y1, x2,y2, x3,y3)
"""
# 使用返回值对线条属性进行设置
# line1,line2 = plt.plot(x, y, 'r-', x, y + 1, 'g-')
# 对line1 进行操作
# line1.set_antialiased(False)  # 关闭抗锯齿
# plt.show()

# 使用plt.setp()函数
line = plt.plot(x, y)
# plt.setp(line, color='g', linewidth=4)
plt.setp(line, 'color', 'r', 'linewidth', 5)
plt.show()


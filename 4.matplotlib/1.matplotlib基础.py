import matplotlib.pyplot as plt
import numpy as np

# 调用 pli.show() 函数 图像才显示
# 默认在新窗口打开一幅图像,并且提供了对图像进行操作的按钮


"""
plt.plot() 函数 绘制线型图
指定x和y : plt.plot(x,y)
默认参数x为0~N-1 : plt.plot(y)
"""
# 缺省参数
plt.plot([1, 2, 3, 4])  # 此处给的值是y
plt.ylabel('y')
plt.xlabel('x')  # 中文字符无法正常显示
# plt.show()

# 传入x,y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()


"""
字符参数
颜色参数:'b':蓝色 blue, 'g':绿色 green, 'r':红色 red, 'c':青色 cyan, 'm':品红 magenta, 'y':黄色 yellow, 'k':黑色 black, 'w':白色 white
类型参数: 省略
"""
# 例如话出红色圆点
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.show()

# 显示范围设置 plt.axis([xmin, xmax, ymin, ymax])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

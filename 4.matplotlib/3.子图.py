import matplotlib.pyplot as plt
import numpy as np

"""
== figure()函数会产生一个指定标号为num的图:plt.figure(num)
    这里 figure(1) 是可以省略的,因为默认情况下plt会自动产生一幅图像
== 使用 subplot可以在一幅图中生成多个子图: plt.subplot(numrows,numcols,fignum)
    当numrows * numcols < 10时,中间的逗号可以省略
"""
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure(figsize=(10, 6))
plt.subplot(211)  # 相当于plt.plot(2,1,1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)  # 相当于plt.plot(2,1,2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

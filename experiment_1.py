import numpy as np
import matplotlib.pyplot as plt

# 设置题目要求的频率
f1 = 1/8
f2 = 5/8
n = np.arange(-32, 33)  # 设置65个采样点，范围是-32 —— +32

# 产生题目要求的信号
x1 = np.cos(2 * np.pi * f1 * n)
x2 = np.cos(2 * np.pi * f2 * n)
x3 = x1 + x2

# 画图
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x1, basefmt=" ")    # basefmt 参数可以去除x轴
plt.title(r'$x_1[n] = \cos(2 \pi f_1 n)$')
plt.xlabel('n')
plt.ylabel('$x_1[n]$')

plt.subplot(3, 1, 2)
plt.stem(n, x2, basefmt=" ")
plt.title(r'$x_2[n] = \cos(2 \pi f_2 n)$')
plt.xlabel('n')
plt.ylabel('$x_2[n]$')

plt.subplot(3, 1, 3)
plt.stem(n, x3, basefmt=" ")
plt.title(r'$x_3[n] = x_1[n] + x_2[n]$')
plt.xlabel('n')
plt.ylabel('$x_3[n]$')

plt.tight_layout()
plt.show()

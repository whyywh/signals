import numpy as np
import matplotlib.pyplot as plt

# 定义信号
f1 = 1/8
f2 = 5/8
n = np.arange(-32, 33)  # 生成65个样本点
x1 = np.cos(2 * np.pi * f1 * n)
x2 = np.cos(2 * np.pi * f2 * n)
x3 = x1 + x2

# 定义系统
h1 = [0.0031, 0.0044, -0.0031, -0.0272, -0.0346, 0.0374, 0.1921, 0.3279, 0.3279, 0.1921, 0.0374, -0.0346, -0.0272,
      -0.0031, 0.0044, 0.0031]
h2 = [-0.0238, 0.0562, -0.0575, -0.1302, 0.5252, -0.6842, -0.3129, 5.6197, 5.6197, -0.3129, -0.6842, 0.5252, -0.1302,
      -0.0575, 0.0562, -0.0238]

# 卷积运算
y1_h1 = np.convolve(x1, h1)
y2_h1 = np.convolve(x2, h1)
y3_h1 = np.convolve(x3, h1)

y1_h2 = np.convolve(x1, h2)
y2_h2 = np.convolve(x2, h2)
y3_h2 = np.convolve(x3, h2)

# 绘制结果
plt.figure(figsize=(12, 12))

# 绘制 h1 系统的输出
plt.subplot(3, 2, 1)
plt.stem(y1_h1, basefmt=" ")
plt.title(r'$y_1[n] = x_1[n] * h_1[n]$')
plt.xlabel('n')
plt.ylabel('$y_1[n]$')

plt.subplot(3, 2, 3)
plt.stem(y2_h1, basefmt=" ")
plt.title(r'$y_2[n] = x_2[n] * h_1[n]$')
plt.xlabel('n')
plt.ylabel('$y_2[n]$')

plt.subplot(3, 2, 5)
plt.stem(y3_h1, basefmt=" ")
plt.title(r'$y_3[n] = x_3[n] * h_1[n]$')
plt.xlabel('n')
plt.ylabel('$y_3[n]$')

# 绘制 h2 系统的输出
plt.subplot(3, 2, 2)
plt.stem(y1_h2, basefmt=" ")
plt.title(r'$y_1[n] = x_1[n] * h_2[n]$')
plt.xlabel('n')
plt.ylabel('$y_1[n]$')

plt.subplot(3, 2, 4)
plt.stem(y2_h2, basefmt=" ")
plt.title(r'$y_2[n] = x_2[n] * h_2[n]$')
plt.xlabel('n')
plt.ylabel('$y_2[n]$')

plt.subplot(3, 2, 6)
plt.stem(y3_h2, basefmt=" ")
plt.title(r'$y_3[n] = x_3[n] * h_2[n]$')
plt.xlabel('n')
plt.ylabel('$y_3[n]$')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 定义参数
f1 = 1/8
f2 = 5/8
n = np.arange(0, 128)  # 生成128个样本点
x1 = np.cos(2 * np.pi * f1 * n)
x2 = np.cos(2 * np.pi * f2 * n)
x3 = x1 + x2

# 定义系统
h1 = [0.0031, 0.0044, -0.0031, -0.0272, -0.0346, 0.0374, 0.1921, 0.3279, 0.3279, 0.1921, 0.0374, -0.0346, -0.0272, -0.0031, 0.0044, 0.0031]
h2 = [-0.0238, 0.0562, -0.0575, -0.1302, 0.5252, -0.6842, -0.3129, 5.6197, 5.6197, -0.3129, -0.6842, 0.5252, -0.1302, -0.0575, 0.0562, -0.0238]

# 计算信号的频谱
def compute_spectrum(signal):
    spectrum = np.fft.fft(signal, 512)
    spectrum = np.fft.fftshift(spectrum)  # 将零频率分量移到中心
    return spectrum

# 计算频谱
X1 = compute_spectrum(x1)
X2 = compute_spectrum(x2)
X3 = compute_spectrum(x3)
H1 = compute_spectrum(h1)
H2 = compute_spectrum(h2)

# 卷积运算
y1_h1 = np.convolve(x1, h1)
y2_h1 = np.convolve(x2, h1)
y3_h1 = np.convolve(x3, h1)

y1_h2 = np.convolve(x1, h2)
y2_h2 = np.convolve(x2, h2)
y3_h2 = np.convolve(x3, h2)

# 计算输出信号的频谱
Y1_H1 = compute_spectrum(y1_h1)
Y2_H1 = compute_spectrum(y2_h1)
Y3_H1 = compute_spectrum(y3_h1)

Y1_H2 = compute_spectrum(y1_h2)
Y2_H2 = compute_spectrum(y2_h2)
Y3_H2 = compute_spectrum(y3_h2)

# 生成频率轴
freqs = np.fft.fftfreq(512, d=1.0)
freqs = np.fft.fftshift(freqs)

# 绘制频谱图
def plot_spectrum(spectrum, title, subplot_index):
    plt.subplot(6, 2, subplot_index)
    plt.plot(freqs, np.abs(spectrum))
    plt.title(title)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')

plt.figure(figsize=(14, 18))

# 输入信号的频谱
plot_spectrum(X1, '$|X_1(e^{j\omega})|$', 1)  # 用$xxxx$括起来的是LaTex的语法
plot_spectrum(X2, '$|X_2(e^{j\omega})|$', 3)
plot_spectrum(X3, '$|X_3(e^{j\omega})|$', 5)

# 系统的频谱
plot_spectrum(H1, '$|H_1(e^{j\omega})|$', 7)
plot_spectrum(H2, '$|H_2(e^{j\omega})|$', 9)

# 输出信号的频谱 (与 h1 卷积)
plot_spectrum(Y1_H1, '$|Y_1(e^{j\omega})| \, {for} \, h_1[n]$', 2)
plot_spectrum(Y2_H1, '$|Y_2(e^{j\omega})| \, {for} \, h_1[n]$', 4)
plot_spectrum(Y3_H1, '$|Y_3(e^{j\omega})| \, {for} \, h_1[n]$', 6)

# 输出信号的频谱 (与 h2 卷积)
plot_spectrum(Y1_H2, '$|Y_1(e^{j\omega})| \, {for} \, h_2[n]$', 8)
plot_spectrum(Y2_H2, '$|Y_2(e^{j\omega})| \, {for} \, h_2[n]$', 10)
plot_spectrum(Y3_H2, '$|Y_3(e^{j\omega})| \, {for} \, h_2[n]$', 12)

plt.tight_layout()
plt.show()



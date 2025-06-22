import numpy as np
import matplotlib.pyplot as plt

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义不同的均值和标准差
mus = [0, 0, 2]
sigmas = [0.5, 1, 1]
colors = ['blue', 'red', 'green']

# 生成 x 轴数据
x = np.linspace(-5, 5, 400)

# 绘制不同参数的正态分布曲线
for mu, sigma, color in zip(mus, sigmas, colors):
    y = 1 / (np.sqrt(2 * np.pi * sigma**2)) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    plt.plot(x, y, color=color, label=f'$\mu$={mu}, $\sigma$={sigma}')

# 添加注释说明
plt.axvline(x=0, color='black', linestyle='--', label='$\mu$ 为对称轴')
plt.text(0, 0.4, '$\mu$ 决定对称轴位置', ha='center', va='center', rotation=90)
plt.text(2, 0.2, '$\sigma$ 越小，曲线越窄', ha='center', va='center')

# 设置图表标题和坐标轴标签
plt.title('正态分布概率密度函数')
plt.xlabel('x')
plt.xticks(rotation=45)
plt.ylabel('概率密度 $f(x)$')

# 显示图例
plt.legend()

# 保存图像
plt.savefig('c:/Users/hhn06/Documents/概率论/normal_distribution.png')

# 显示图表
plt.show()

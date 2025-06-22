import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成 x 轴数据
x = np.linspace(-5, 5, 1000)

# 计算标准正态分布的概率密度函数值
pdf = norm.pdf(x, 0, 1)

# 计算标准正态分布的分布函数值
cdf = norm.cdf(x, 0, 1)

# 创建一个包含两个子图的画布，修改为 1 行 2 列
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 绘制概率密度函数
axs[0].plot(x, pdf, label=r'概率密度函数 $f(x)$')
axs[0].fill_between(x, pdf, alpha=0.3)
# 设置标题和坐标轴标签，并调整字体大小
axs[0].set_title('标准正态分布的概率密度函数 $f(x)$', fontsize=12)
axs[0].set_xlabel('x', fontsize=10)
axs[0].set_ylabel('概率密度', fontsize=10)
axs[0].legend(fontsize=10)

# 绘制分布函数
axs[1].plot(x, cdf, label=r'分布函数 $F(x)$', color='orange')
# 设置标题和坐标轴标签，并调整字体大小
axs[1].set_title('标准正态分布的分布函数 $F(x)$', fontsize=12)
axs[1].set_xlabel('x', fontsize=10)
axs[1].set_ylabel('累积概率', fontsize=10)
axs[1].legend(fontsize=10)

# 自动调整子图参数，使之填充整个图像区域
plt.tight_layout()

# 保存图片，可根据需要修改保存路径和文件名
plt.savefig('standard_normal_distribution.png', dpi=300)

plt.show()
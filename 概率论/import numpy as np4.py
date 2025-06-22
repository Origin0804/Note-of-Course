import numpy as np
import matplotlib.pyplot as plt

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义不同的 lambda 值
lambdas = [0.5, 1, 2]
colors = ['blue', 'red', 'green']

# 生成 x 轴数据
x = np.linspace(0, 10, 400)

# 绘制不同参数的指数分布曲线
for lam, color in zip(lambdas, colors):
    y = np.where(x >= 0, lam * np.exp(-lam * x), 0)
    plt.plot(x, y, color=color, label=f'$\lambda$={lam}')

# 设置图表标题和坐标轴标签
plt.title('指数分布概率密度函数')
plt.xlabel('x')
plt.xticks(rotation=45)
plt.ylabel('概率密度 $f(x)$')

# 显示图例
plt.legend()

# 保存图像
plt.savefig('c:/Users/hhn06/Documents/概率论/exponential_distribution.png')

# 显示图表
plt.show()

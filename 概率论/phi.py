import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 指定支持中文的字体，这里以黑体为例，不同系统可能字体名称不同
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统常用黑体
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # Linux系统常用文泉驿正黑
# plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']  # Mac系统常用冬青黑体

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False


# 定义参数
mu_x = 0
mu_y = 0
sigma_x = 1
sigma_y = 1
rho_values = [-0.8, 0, 0.8]

# 生成网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(15, 5))

for i, rho in enumerate(rho_values):
    # 计算二维正态分布的概率密度函数
    Z = (1 / (2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2))) * \
        np.exp(-((((X - mu_x) / sigma_x)**2 - 2 * rho * ((X - mu_x) / sigma_x) * ((Y - mu_y) / sigma_y) + ((Y - mu_y) / sigma_y)**2) / (2 * (1 - rho**2))))

    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(f'rho = {rho}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

# 保存图片，可根据需要修改保存路径和文件名
plt.savefig('phi.png', dpi=300, bbox_inches='tight')


plt.tight_layout()
plt.show()

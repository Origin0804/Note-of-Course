import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 指定支持中文的字体，这里以黑体为例，不同系统可能字体名称不同
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统常用黑体
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # Linux系统常用文泉驿正黑
# plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']  # Mac系统常用冬青黑体

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 定义二维正态分布的参数
mu_x = 0  # X 的均值
mu_y = 0  # Y 的均值
sigma_x = 1  # X 的标准差
sigma_y = 1  # Y 的标准差
rho = 0  # X 和 Y 的相关系数

# 生成网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算二维正态分布的概率密度函数
Z = (1 / (2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2))) * \
    np.exp(-((((X - mu_x) / sigma_x)**2 - 2 * rho * ((X - mu_x) / sigma_x) * ((Y - mu_y) / sigma_y) + ((Y - mu_y) / sigma_y)**2) / (2 * (1 - rho**2))))

# 创建 3D 图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面图
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 设置坐标轴标签，将概率密度竖向显示
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('二维正态分布')

# 保存图片，可根据需要修改保存路径和文件名
plt.savefig('normal_distribution_2d.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

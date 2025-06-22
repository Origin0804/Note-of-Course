import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 定义二维正态分布的概率密度函数
def pdf(x, y, mu_x=0, mu_y=0, sigma_x=1, sigma_y=1):
    exponent = -((x - mu_x) ** 2 / (2 * sigma_x ** 2) + (y - mu_y) ** 2 / (2 * sigma_y ** 2))
    return np.exp(exponent) / (2 * np.pi * sigma_x * sigma_y)

# 生成二维正态分布的数据
x_grid = np.linspace(-5, 5, 100)
y_grid = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = pdf(X, Y)

# 定义微粒数量
num_particles = 100
# 模拟时间步数
num_steps = 50

# 初始化微粒的位置
x_particles = np.random.uniform(-5, 5, num_particles)
y_particles = np.random.uniform(-5, 5, num_particles)
z_particles = np.zeros(num_particles)

# 定义下落速度
fall_speed = 0.1

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制二维正态分布的曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

# 初始化微粒的散点图
scat = ax.scatter(x_particles, y_particles, z_particles, c='b', s=10)

# 设置坐标轴范围
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 0.2)

# 定义更新函数
def update(frame):
    global z_particles
    # 微粒下落
    z_particles -= fall_speed
    # 当微粒落到 z = 0 时，重新初始化其位置
    reset_indices = z_particles < 0
    z_particles[reset_indices] = 0.2
    x_particles[reset_indices] = np.random.uniform(-5, 5)
    y_particles[reset_indices] = np.random.uniform(-5, 5)

    # 更新散点图的数据
    scat._offsets3d = (x_particles, y_particles, z_particles)
    return scat,

# 创建动画
ani = FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)

# 显示动画
plt.show()

# 保存动画
ani.save('particle_fall_with_distribution.gif', writer='pillow')
print("动画已保存为 'particle_fall_with_distribution.gif'")

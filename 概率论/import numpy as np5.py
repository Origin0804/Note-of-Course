import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 定义微粒数量
num_particles = 100
# 模拟时间步数
num_steps = 50

# 初始化微粒的位置
x = np.random.uniform(-5, 5, num_particles)
y = np.random.uniform(-5, 5, num_particles)
z = np.zeros(num_particles)

# 定义下落速度
fall_speed = 0.1

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 初始化散点图
scat = ax.scatter(x, y, z, c='b', s=10)

# 设置坐标轴范围
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 5)

# 定义更新函数
def update(frame):
    global z
    # 微粒下落
    z -= fall_speed
    # 当微粒落到 z = 0 时，重新初始化其位置
    reset_indices = z < 0
    z[reset_indices] = 5
    x[reset_indices] = np.random.uniform(-5, 5)
    y[reset_indices] = np.random.uniform(-5, 5)

    # 更新散点图的数据
    scat._offsets3d = (x, y, z)
    return scat,

# 创建动画
ani = FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)

# 显示动画
plt.show()

# 保存动画（可选）
# ani.save('particle_fall.gif', writer='pillow')
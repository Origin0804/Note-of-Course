import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# 自定义 3D 箭头类
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        # 从 self.axes.M 获取投影矩阵
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

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

# 初始化微粒的位置
x_particles = np.random.uniform(-5, 5, num_particles)
y_particles = np.random.uniform(-5, 5, num_particles)
# 随机初始化微粒的高度，模拟下落过程中的某个时刻
z_particles = np.random.uniform(0, 0.2, num_particles)

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制二维正态分布的曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 绘制微粒的散点图
scat = ax.scatter(x_particles, y_particles, z_particles, c='b', s=10)

# 绘制尾迹线或箭头
fall_distance = 0.03  # 尾迹线或箭头的长度
for i in range(num_particles):
    x = x_particles[i]
    y = y_particles[i]
    z = z_particles[i]
    # 绘制尾迹线
    ax.plot([x, x], [y, y], [z, z - fall_distance], color='gray', linewidth=0.5)
    # 绘制箭头
    a = Arrow3D([x, x], [y, y], [z, z - fall_distance], mutation_scale=5,
                lw=1, arrowstyle="-|>", color="r")
    ax.add_artist(a)

# 设置坐标轴范围
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 0.2)

# 显示图形
plt.show()

# 保存图形（可选）
fig.savefig('particle_fall_with_distribution_single_frame.png', dpi=300)
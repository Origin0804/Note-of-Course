import numpy as np
import matplotlib.pyplot as plt

# 定义均匀分布的参数
a = 1
b = 5

# 生成 x 轴数据
x = np.linspace(a - 2, b + 2, 400)

# 定义均匀分布的概率密度函数
def uniform_pdf(x, a, b):
    result = np.zeros_like(x)
    mask = (x >= a) & (x <= b)
    result[mask] = 1 / (b - a)
    return result

# 计算 y 轴数据
y = uniform_pdf(x, a, b)

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 绘制图像
plt.plot(x, y, label='Uniform Distribution PDF')
plt.fill_between(x, y, alpha=0.3)
plt.title('Probability Density Function of Uniform Distribution')
plt.xlabel('x')
plt.xticks(rotation=45)
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# 保存图像
plt.savefig('uniform_distribution.png')

# 显示图像
plt.show()

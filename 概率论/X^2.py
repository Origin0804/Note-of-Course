import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# 设置x轴范围
x = np.linspace(0, 10, 1000)

# 设置不同自由度的卡方分布
dfs = [1, 2, 3, 4, 5]  # 自由度列表
colors = ['red', 'blue', 'green', 'purple', 'orange']  # 每条曲线的颜色

plt.figure(figsize=(4, 3))

# 绘制不同自由度的卡方分布曲线
for df, color in zip(dfs, colors):
    plt.plot(x, chi2.pdf(x, df), 
             color=color, 
             label=f'df={df}')

# 添加图表元素
plt.title('Chi-Square Distribution with Different Degrees of Freedom')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.savefig('chi-square-distribution.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()

import matplotlib.pyplot as plt
import networkx as nx
import os

# 创建思维导图的结构
mindmap = {
    "课程教学重点": {
        "绪论与力学基础": ["课程介绍", "力、力矩、力系", "静力学基本公理"],
        "力系分析": ["平面力系平衡", "空间力系简化与平衡", "主矢主矩"],
        "摩擦与变形": ["滑动摩擦、自锁", "轴向拉压", "应力应变、胡克定律"],
        "扭转与弯曲": ["剪切与扭转", "圆轴扭转应力", "弯曲应力与内力图"],
        "稳定性与动力学": ["压杆稳定性", "点与刚体运动", "动量动能定理"],
    }
}

# 绘制思维导图
G = nx.DiGraph()

# 添加根节点
G.add_node("课程教学重点", level=0)

# 添加子节点
for branch, topics in mindmap["课程教学重点"].items():
    G.add_node(branch, level=1)
    G.add_edge("课程教学重点", branch)
    for topic in topics:
        G.add_node(topic, level=2)
        G.add_edge(branch, topic)

# 创建更美观的图形布局 - 使用shell_layout，根据层级排列节点
levels = {}
for node in G.nodes:
    level = G.nodes[node].get('level', 0)
    if level not in levels:
        levels[level] = []
    levels[level].append(node)

# 为不同层级的节点设置不同的半径
radius = [0, 3, 6]  # 调整这些值来控制层级之间的距离
pos = {}
for i, level in enumerate(sorted(levels.keys())):
    # 为每个层级的节点创建圆形排列
    nodes = levels[level]
    angle_step = 2 * 3.14159 / len(nodes)
    for j, node in enumerate(nodes):
        angle = j * angle_step
        pos[node] = (radius[i] * 2 * 3.14159 / len(nodes) * j, radius[i])

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC", "Microsoft YaHei"]

# 检查系统平台，确保路径正确
if os.name == 'nt':  # Windows系统
    output_dir = os.path.join(os.getcwd(), "data")
else:  # Linux/Mac系统
    output_dir = "/mnt/data"

# 创建保存目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "教学重点思维导图_v3.png")

# 为不同层级的节点设置不同的颜色
node_colors = []
for node in G.nodes:
    level = G.nodes[node].get('level', 0)
    if level == 0:
        node_colors.append("#FF9999")  # 根节点颜色
    elif level == 1:
        node_colors.append("#99CCFF")  # 一级节点颜色
    else:
        node_colors.append("#CCFF99")  # 二级节点颜色

# 为不同层级的节点设置不同的大小
node_sizes = []
for node in G.nodes:
    level = G.nodes[node].get('level', 0)
    if level == 0:
        node_sizes.append(7000)  # 根节点大小
    elif level == 1:
        node_sizes.append(5000)  # 一级节点大小
    else:
        node_sizes.append(3500)  # 二级节点大小

# 绘制图形
plt.figure(figsize=(14, 12))

# 绘制节点和边
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1.5, edge_color='gray', alpha=0.7)
nx.draw_networkx_labels(G, pos, font_family=plt.rcParams["font.family"], font_size=10, font_weight='bold')

# 添加标题
plt.title("课程教学重点思维导图", fontsize=18, fontweight='bold')

# 调整布局，使节点分布更合理
plt.axis('off')
plt.tight_layout()

# 保存并展示图像
try:
    plt.savefig(output_path, format="png", dpi=300, bbox_inches='tight')
    print(f"图像已成功保存到: {output_path}")
except Exception as e:
    print(f"保存图像时出错: {e}")
    # 如果保存失败，尝试使用默认路径
    output_path = "教学重点思维导图_v3.png"
    plt.savefig(output_path, format="png", dpi=300, bbox_inches='tight')
    print(f"已使用替代路径保存图像: {os.path.abspath(output_path)}")

plt.show()

print(f"图像路径: {output_path}")
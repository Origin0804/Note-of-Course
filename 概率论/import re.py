import re

# 文档路径
file_path = 'c:/Users/hhn06/Documents/概率论/概率论.md'

try:
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式替换组合数
    pattern = r'\\binom\{([^}]+)\}\{([^}]+)\}'
    def replace_combination(match):
        a = match.group(1)
        b = match.group(2)
        return f'C_{{{a}}}^{{{b}}}'

    new_content = re.sub(pattern, replace_combination, content)

    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print("组合数替换完成。")
except FileNotFoundError:
    print(f"未找到文件: {file_path}")
except Exception as e:
    print(f"处理文件时出错: {e}")

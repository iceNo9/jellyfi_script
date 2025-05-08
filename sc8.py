import os
import re

# 定义需要处理的目录路径

# 替换为实际路径
base_path = r'\\Nas-hupo\blue\temp2'

def clean_folder_name(name):
    # 移除形如 [xxx] 的内容
    name = re.sub(r'\[.*?\]', '', name)
    # 移除 'OVA'，大小写不敏感
    name = re.sub(r'(?i)OVA', '', name)
    # 去掉开头和结尾空白字符（包括多余空格、制表符等）
    return name.strip()

def rename_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for folder in dirs:
            old_path = os.path.join(root, folder)
            new_name = clean_folder_name(folder)
            new_path = os.path.join(root, new_name)
            if old_path != new_path:
                if not os.path.exists(new_path):
                    print(f"重命名: '{old_path}' -> '{new_path}'")
                    os.rename(old_path, new_path)
                else:
                    print(f"跳过: 目标已存在 '{new_path}'")

if __name__ == '__main__':
    rename_folders(base_path)


# 移除[xxx]的部分，并去掉开头和结尾空白字符
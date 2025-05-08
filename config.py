import os

# 基础路径
BASE_DIR = r""

# 获取该目录下所有子文件夹（不包括文件）
subdirs = [
    os.path.join(BASE_DIR, d)
    for d in os.listdir(BASE_DIR)
    if os.path.isdir(os.path.join(BASE_DIR, d))
]

# 如果没有子文件夹就抛出异常
if not subdirs:
    raise FileNotFoundError("未找到任何子文件夹")

# 找到最新创建的文件夹
latest_folder = max(subdirs, key=os.path.getctime)

# 标准化路径
ROOT_DIR = os.path.normpath(latest_folder)

# 测试输出
print("最新创建的文件夹为：", ROOT_DIR)


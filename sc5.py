import os
import re

# ====== 配置项 ======

# 修改为你的文件夹路径
folder_path = r"F:\BaiduNetdiskDownload\2025-5-6\月出之战\Season 1"  
file_extensions = [".mp4", ".mkv", ".avi", ".sc.ass", ".tc.ass"]  # 要处理的文件类型，可以自行添加扩展名
# ===================

# 正则模式：匹配如 [S01E05] 或 [s01e05]
pattern = re.compile(r"^\[S\d{2}E\d{2}\]\s*", re.IGNORECASE)

# 遍历文件夹
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # 检查是否是文件，并检查扩展名
    if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in file_extensions):
        # 如果文件名匹配前缀
        if pattern.match(filename):
            new_filename = pattern.sub("", filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")


# 去除前缀[S**E**]
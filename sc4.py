import os

# === 配置区域 ===
folder_path = r"\\NAS-hupo\media\anime\秦时明月\Season 6 - 沧海横流 (Canghai Hengliu)"    # 要处理的文件夹
valid_suffixes = ['mp4']     # 完整后缀匹配（首个 `.` 之后的部分）
season_number = 6                      # 当前季数
start_episode = 1                      # 起始集数
# =================

def get_custom_suffix(filename):
    """获取第一个`.`之后的部分（含多个`.`的文件支持）"""
    parts = filename.split('.', 1)
    return parts[1] if len(parts) > 1 else ''

def format_prefix(season, episode):
    return f"[S{season:02d}E{episode:02d}]"

def add_prefix_to_files():
    if not os.path.isdir(folder_path):
        print(f"目录不存在: {folder_path}")
        return

    files = sorted(os.listdir(folder_path))
    matched_files = []

    for f in files:
        suffix = get_custom_suffix(f)
        if suffix.lower() in valid_suffixes:
            matched_files.append(f)

    if not matched_files:
        print("未找到匹配文件")
        return

    episode = start_episode
    for filename in matched_files:
        prefix = format_prefix(season_number, episode)
        if filename.startswith(prefix):
            print(f"跳过已有前缀文件: {filename}")
            episode += 1
            continue

        new_filename = f"{prefix} {filename}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        print(f"重命名: {filename} → {new_filename}")
        os.rename(old_path, new_path)
        episode += 1

    print("处理完成。")

if __name__ == "__main__":
    add_prefix_to_files()


# 格式化视频名称
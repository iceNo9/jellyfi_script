import os
from config import ROOT_DIR

# === 配置区 ===

base_dir = ROOT_DIR

# 创建 Season 1 到 Season N 的文件夹
max_season = 2

# === 执行创建 ===
def create_season_folders(base, max_season):
    for season in range(1, max_season + 1):
        folder_name = f"Season {season}"
        season_path = os.path.join(base, folder_name)

        if not os.path.exists(season_path):
            os.makedirs(season_path)
            print(f"已创建文件夹: {season_path}")
        else:
            print(f"文件夹已存在: {season_path}")

create_season_folders(base_dir, max_season)


# 批量创建season 文件夹
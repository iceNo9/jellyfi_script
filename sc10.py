import os
import re
from collections import defaultdict

# === 配置扩展名 ===
main_extensions = ['mp4', 'mkv', 'avi']
aux_extensions = [
    '繁體中文.ass', '简体中文.ass', 'SC.ass', 'sc.ass', 'sc.srt',
    'TC.ass', 'tc.ass', 'tc.srt', 'ass', 'srt'
]

# 获取完整扩展名
def get_ext_by_dot(filename):
    parts = filename.split('.')
    return '.'.join(parts[1:]) if len(parts) > 1 else ''

# 重命名一个 Season 文件夹
def process_season_folder(season_path):
    season_pattern = re.compile(r'Season\s*(\d+)', re.IGNORECASE)
    entry = os.path.basename(season_path)
    season_match = season_pattern.match(entry)
    if not season_match:
        print(f"跳过非 Season 文件夹: {season_path}")
        return

    season_num = int(season_match.group(1))
    season_str = f"S{season_num:02d}"

    files = os.listdir(season_path)
    main_files = []
    aux_files_by_ext = defaultdict(list)

    for file in files:
        filepath = os.path.join(season_path, file)
        if not os.path.isfile(filepath):
            continue

        ext = get_ext_by_dot(file)
        if ext in main_extensions:
            main_files.append(file)
        elif ext in aux_extensions:
            aux_files_by_ext[ext].append(file)

    main_files.sort()
    for ext_list in aux_files_by_ext.values():
        ext_list.sort()

    for idx, filename in enumerate(main_files, start=1):
        ep_str = f"E{idx:02d}"
        new_name = f"[{season_str}{ep_str}] {filename}"
        os.rename(
            os.path.join(season_path, filename),
            os.path.join(season_path, new_name)
        )
        print(f"主文件重命名: {filename} -> {new_name}")

    for ext, files in aux_files_by_ext.items():
        for idx, filename in enumerate(files):
            if idx >= len(main_files):
                print(f"辅助文件 {filename}（类型 {ext}）超出主文件数量，跳过")
                continue
            ep_str = f"E{idx+1:02d}"
            new_name = f"[{season_str}{ep_str}] {filename}"
            os.rename(
                os.path.join(season_path, filename),
                os.path.join(season_path, new_name)
            )
            print(f"辅助文件重命名（{ext}）: {filename} -> {new_name}")

# 遍历所有番剧目录，对其中的 Season 子目录执行处理
def process_all_anime_under(root_dir):
    for anime_name in os.listdir(root_dir):
        anime_path = os.path.join(root_dir, anime_name)
        if not os.path.isdir(anime_path):
            continue

        print(f"\n📁 处理番剧目录: {anime_name}")
        for season_entry in os.listdir(anime_path):
            season_path = os.path.join(anime_path, season_entry)
            if os.path.isdir(season_path):
                process_season_folder(season_path)

# === 设置根目录，注意：这个目录下是多个番剧文件夹 ===
multi_anime_root = r"\\Nas-hupo\docker\alist\alist_1\local\影视学习2025-5-7"
process_all_anime_under(multi_anime_root)


import os
import re
from collections import defaultdict

# === 用户配置 ===

root_dir = r"F:\BaiduNetdiskDownload\2025-5-6\月出之战"

main_extensions = ['mp4', 'mkv', 'avi']
aux_extensions = ['繁體中文.ass', '简体中文.ass','SC.ass','sc.ass', 'sc.srt', 'TC.ass', 'tc.ass', 'tc.srt', 'ass', 'srt']

# 获取完整扩展名
def get_ext_by_dot(filename):
    return '.'.join(filename.split('.')[1:]) if '.' in filename else ''

season_pattern = re.compile(r'Season\s*(\d+)', re.IGNORECASE)

for entry in os.listdir(root_dir):
    full_path = os.path.join(root_dir, entry)
    if not os.path.isdir(full_path):
        continue

    season_match = season_pattern.match(entry)
    if not season_match:
        continue

    season_num = int(season_match.group(1))
    season_str = f"S{season_num:02d}"

    files = os.listdir(full_path)
    main_files = []
    aux_files_by_ext = defaultdict(list)

    for file in files:
        filepath = os.path.join(full_path, file)
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

    # 重命名主文件
    for idx, filename in enumerate(main_files, start=1):
        ep_str = f"E{idx:02d}"
        new_name = f"[{season_str}{ep_str}] {filename}"
        os.rename(
            os.path.join(full_path, filename),
            os.path.join(full_path, new_name)
        )
        print(f"主文件重命名: {filename} -> {new_name}")

    # 重命名辅助文件，按每种扩展分别处理
    for ext, files in aux_files_by_ext.items():
        for idx, filename in enumerate(files):
            if idx >= len(main_files):
                print(f"辅助文件 {filename}（类型 {ext}）超出主文件数量，跳过")
                continue
            ep_str = f"E{idx+1:02d}"
            new_name = f"[{season_str}{ep_str}] {filename}"
            os.rename(
                os.path.join(full_path, filename),
                os.path.join(full_path, new_name)
            )
            print(f"辅助文件重命名（{ext}）: {filename} -> {new_name}")

# 番剧 的 视频字幕重命名
import os
import re
import sys

def rename_files_with_new_season(folder_path, season_number=2, extensions=('.mp4', '.mkv', '.avi')):
    if not os.path.isdir(folder_path):
        print(f"❌ 无效目录: {folder_path}")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith(extensions)]
    files.sort()  # 按文件名排序，保证顺序编号一致

    for index, filename in enumerate(files):
        # 移除所有类似 S01E15 的部分（区分大小写，防止误杀）
        cleaned_name = re.sub(r'[.\-_ ]?S\d{2}E\d{2}', '', filename, flags=re.IGNORECASE)

        # 生成新前缀
        episode_number = index + 1
        new_prefix = f"[S{season_number:02d}E{episode_number:02d}]"

        # 拼接新文件名
        new_filename = new_prefix + cleaned_name

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        print(f"✅ 重命名: {filename} → {new_filename}")
        os.rename(old_path, new_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python rename_season2.py \"\\\\NAS-hupo\\media\\anime\\...\"")
    else:
        folder_path = sys.argv[1]
        rename_files_with_new_season(folder_path)

import os
import shutil
from config import ROOT_DIR

# === 配置区 ===
root_dir = ROOT_DIR
image_extensions = [".png", ".jpg", ".jpeg"]
video_extensions = [".mkv", ".mp4", ".tc.ass", ".sc.ass", ".ass", ".srt"]
nfo_extension = ".nfo"

# 提取季数
def get_season_number(directory):
    folder_name = os.path.basename(directory)
    if "Season" in folder_name:
        try:
            return int(folder_name.split("Season")[-1].strip())
        except ValueError:
            return None
    return None

def format_season(season):
    return f"season{season:02d}"

# 提取完整扩展名（匹配列表中最长的后缀）
def get_full_extension(filename, ext_list):
    for ext in sorted(ext_list, key=lambda e: -len(e)):
        if filename.lower().endswith(ext):
            return ext
    return None

def process_files_for_seasons(root, image_exts, video_exts):
    for dirpath, dirnames, filenames in os.walk(root):
        for dir_name in dirnames:
            season_number = get_season_number(dir_name)
            if season_number is None:
                continue

            season_folder = os.path.join(dirpath, dir_name)
            file_list = os.listdir(season_folder)

            # 处理 fanart / poster 图像
            for filename in file_list:
                if not any(filename.lower().endswith(ext) for ext in image_exts):
                    continue

                if "-poster" in filename:
                    suffix = "-poster"
                elif "-fanart" in filename:
                    suffix = "-fanart"
                else:
                    continue

                ext = os.path.splitext(filename)[1]
                new_filename = format_season(season_number) + suffix + ext
                src_path = os.path.join(season_folder, filename)
                dst_path = os.path.join(os.path.dirname(season_folder), new_filename)

                if os.path.abspath(src_path) != os.path.abspath(dst_path):
                    print(f"Copying: {src_path} → {dst_path}")
                    shutil.copy2(src_path, dst_path)

            # 处理视频重命名逻辑（支持复合后缀）
            nfo_files = [f for f in file_list if f.lower().endswith(nfo_extension)]
            video_files = [f for f in file_list if get_full_extension(f, video_exts)]

            if len(nfo_files) == 1:
                nfo_base = os.path.splitext(nfo_files[0])[0]
                for video_file in video_files:
                    video_ext = get_full_extension(video_file, video_exts)
                    if not video_ext:
                        continue

                    src_video_path = os.path.join(season_folder, video_file)
                    dst_video_path = os.path.join(season_folder, nfo_base + video_ext)

                    if os.path.abspath(src_video_path) != os.path.abspath(dst_video_path):
                        print(f"Renaming: {src_video_path} → {dst_video_path}")
                        os.rename(src_video_path, dst_video_path)

process_files_for_seasons(root_dir, image_extensions, video_extensions)


# 里番视频/图片处理
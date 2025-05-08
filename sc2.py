import os

# === 配置区 ===
video_dir = r"F:\BaiduNetdiskDownload\[Snow-Raws] ご注文はうさぎですか？？ 第二季"        # 视频所在目录
subtitle_dir = r"C:\Users\hupo9\Downloads\[zmk.pw][澄空学园&华盟字幕社][请问您今天要来点兔子吗 第1-2季][简体外挂字幕][TVrip][720P]\[澄空学园&华盟字幕社][请问您今天要来点兔子吗 第1-2季][简体外挂字幕][TVrip][720P]\S2"      # 字幕所在目录
video_exts = ['.mkv', '.mp4', '.avi']     # 支持的视频扩展名
subtitle_ext = ".ass"                     # 要处理的字幕扩展名
# =============

def rename_subtitles():
    if not os.path.isdir(video_dir):
        print(f"视频目录无效: {video_dir}")
        return
    if not os.path.isdir(subtitle_dir):
        print(f"字幕目录无效: {subtitle_dir}")
        return

    # 获取所有视频文件（按名字排序）
    video_files = sorted([
        f for f in os.listdir(video_dir)
        if os.path.splitext(f)[1].lower() in video_exts
    ])

    # 获取所有字幕文件（按名字排序）
    subtitle_files = sorted([
        f for f in os.listdir(subtitle_dir)
        if f.lower().endswith(subtitle_ext)
    ])

    if len(subtitle_files) < len(video_files):
        print(f"字幕数量不足：视频有 {len(video_files)} 个，字幕只有 {len(subtitle_files)} 个。")
        return

    for i, video_file in enumerate(video_files):
        video_name, _ = os.path.splitext(video_file)
        subtitle_file = subtitle_files[i]
        old_sub_path = os.path.join(subtitle_dir, subtitle_file)
        new_sub_path = os.path.join(subtitle_dir, f"{video_name}{subtitle_ext}")

        print(f"重命名: {subtitle_file} → {video_name}{subtitle_ext}")
        os.rename(old_sub_path, new_sub_path)

    print("字幕重命名完成。")

if __name__ == '__main__':
    rename_subtitles()

# 传颂之物修改字幕文件名称
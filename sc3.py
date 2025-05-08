import os

# ======= 配置区域 =======
folder_path = r"C:\Users\hupo9\Downloads\[zmk.pw][白月字幕组×VCB-Studio][请问您今天要来点兔子吗？][第1季][简繁外挂字幕][BDrip][1080P]\[白月字幕组×VCB-Studio][请问您今天要来点兔子吗？][第1季][简繁外挂字幕][BDrip][1080P]\TC"  # 替换成你的字幕文件夹路径
source_exts = [".ass"]  # 支持的原始字幕扩展名
target_ext = "tc"  # 目标中间名，例如 tc，最终会变成 xxx.tc.ass
# =======================

def rename_subtitle_files(folder):
    for file in os.listdir(folder):
        lower_file = file.lower()

        for ext in source_exts:
            if lower_file.endswith(ext):
                full_path = os.path.join(folder, file)

                # 找到第一个 '.'，分离前缀名和其后的部分
                first_dot = file.find(".")
                if first_dot == -1:
                    continue  # 没有点，跳过

                name_prefix = file[:first_dot]
                new_filename = f"{name_prefix}.{target_ext}{ext}"

                if file == new_filename:
                    continue  # 不需要改名

                new_path = os.path.join(folder, new_filename)
                os.rename(full_path, new_path)
                print(f"Renamed: {file} -> {new_filename}")
                break  # 匹配到一个扩展就跳出 inner 循环

if __name__ == "__main__":
    rename_subtitle_files(folder_path)


# 改字幕支持的名字
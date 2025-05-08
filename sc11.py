import os
import Levenshtein

# 定义两个文件夹路径
folder1 = r'\\NAS-hupo\media\anime'
folder2 = r'\\Nas-hupo\docker\alist\alist_1\local\影视学习2025-5-7'

# 设置匹配相似度阈值（1.0 为完全相同，0.0 为完全不同）
SIMILARITY_THRESHOLD = 0.8

def get_subfolder_names(path):
    return [name for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))]

def find_similar_folders(folders1, folders2, threshold):
    similar_pairs = []
    for name1 in folders1:
        for name2 in folders2:
            similarity = Levenshtein.ratio(name1, name2)
            if similarity >= threshold:
                similar_pairs.append((name1, name2, similarity))
    return similar_pairs

if __name__ == '__main__':
    subfolders1 = get_subfolder_names(folder1)
    subfolders2 = get_subfolder_names(folder2)

    matches = find_similar_folders(subfolders1, subfolders2, SIMILARITY_THRESHOLD)

    print(f"相似文件夹（相似度 ≥ {SIMILARITY_THRESHOLD}）:")
    for name1, name2, similarity in matches:
        print(f"{name1}  <-->  {name2}  (相似度: {similarity:.2f})")

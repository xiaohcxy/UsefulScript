# 计算输入目录下的所有文件夹大小并降序输出
import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            file_path = os.path.join(path, f)
            total_size += os.path.getsize(file_path)
    return total_size

def get_directory_sizes(directory_path):
    directory_sizes = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            directory_sizes[item] = get_folder_size(item_path)
    return directory_sizes

def convert_bytes_to_gb(size_in_bytes):
    gb_size = size_in_bytes / (1024 * 1024 * 1024)
    return gb_size

# 获取用户输入的目录路径
directory_path = input("请输入目录路径: ")

# 检查目录是否存在
if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
    print("目录路径无效！")
else:
    directory_sizes = get_directory_sizes(directory_path)
    sorted_sizes = sorted(directory_sizes.items(), key=lambda x: x[1], reverse=True)
    for directory, size in sorted_sizes:
        size_gb = convert_bytes_to_gb(size)
        print(f"{directory}: {size_gb:.2f} GB")

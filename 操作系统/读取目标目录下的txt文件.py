import os

def filter_files_with_txt(file_list_file, directory, destination_folder):
    # 读取包含文件名的文本文件
    with open(file_list_file, 'r') as f:
        file_names = f.read().splitlines()

    file_names_with_extension = [file_name + '.txt' for file_name in file_names]

    # 筛选文件夹中的文件
    filtered_files = []
    for file_name in file_names_with_extension:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            filtered_files.append(file_path)

 # 复制文件到目标文件夹
    for file_path in filtered_files:
        destination_path = os.path.join(destination_folder, os.path.basename(file_path))
        with open(file_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
            destination_file.write(source_file.read())

    return filtered_files

# 指定包含文件名的文本文件和文件夹路径
file_list_file = ""
directory = ""
destination_folder = ""

# 进行文件筛选
filtered_files = filter_files_with_txt(file_list_file, directory, destination_folder)

# 打印筛选结果
for file_path in filtered_files:
    print(file_path)

import os
import shutil

# 指定文件路径
file_path = "G:/1102_data_check/train_20241012.txt"
# 打开文件并读取内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

target_folder = "G:/1102_data_check/liutao_chinese_r0.7"

target_files = os.listdir(target_folder)
output_dir = "G:/1102_data_check/liutao_chinses_r0.7_Filtered"

# 打印文件内容



filtered_files = []

for file_name in target_files:
    print(file_name)
    if file_name in content:
        print("Yes")
        filtered_files.append(file_name)
        source_path = os.path.join(target_folder, file_name)
        output_path = os.path.join(output_dir, file_name)
        shutil.copy(source_path, output_path)


    else:
        print("No")


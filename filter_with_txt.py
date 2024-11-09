import os
import shutil
import json


# 指定文件路径
# file_path = "G:/1102_data_check/train_20241012.txt"
# # 打开文件并读取内容
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
#
# target_folder = "G:/1102_data_check/liutao_chinese_r0.7"
#
# target_files = os.listdir(target_folder)
# output_dir = "G:/1102_data_check/liutao_chinses_r0.7_Filtered"

# 打印文件内容


#json input

file_path = 'liutao_handfilter_list.json'

with open(file_path, 'r', encoding='utf-8') as file1:
    content = json.load(file1)


new_content = []
for item in content:
    new_content.append(item+".mp4")
content = new_content

print(content)

target_folder = "liutao_chinses_r0.7_Filtered"
target_files = os.listdir(target_folder)
hand_output_dir = "liutao_withhand"
nohand_output_dir = "liutao_nohand"

filtered_files = []

for file_name in target_files:
    print(file_name)
    if file_name in content:
        print("Yes")
        filtered_files.append(file_name)
        source_path = os.path.join(target_folder, file_name)
        output_path = os.path.join(hand_output_dir, file_name)
        shutil.copy(source_path, output_path)

    else:
        print("No")
        source_path = os.path.join(target_folder, file_name)
        output_path = os.path.join(nohand_output_dir, file_name)
        shutil.copy(source_path, output_path)



# tecent 97
# NO HAND : 1
# HAND :
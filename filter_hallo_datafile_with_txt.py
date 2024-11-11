import os
import shutil
import json



file_path = 'liutao_handfilter_list_r02.json'

with open(file_path, 'r', encoding='utf-8') as file1:
    content = json.load(file1)

file_path2 = "hallo_liutao_cn_stage1.json"

with open(file_path2, 'r', encoding='utf-8') as file1:
    content2 = json.load(file1)



output = []
output_path = "hallo_liutao_cn_r02_stage1.json"
#print(content)

for data_dict in content2:
    image_path = data_dict["image_path"]
    folder_name = os.path.basename(image_path)
    print(folder_name)
    if folder_name in content:

        print("yes")
        output.append(data_dict)
    else:
        print("No")

print(len(output))
#
# chdtf_num_55640015262d1311cc0ecde1eaefbdcf_004
with open(output_path, 'w', encoding='utf-8') as file:
    # 将字典转换为json格式并写入文件
    json.dump(output, file, ensure_ascii=False, indent=4)


# tecent 97
# NO HAND : 1
# HAND :
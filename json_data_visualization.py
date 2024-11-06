import json
import matplotlib.pyplot as plt

good_count_path = 'file1.json'
good_conf_path = 'file2.json'
bad_count_path = 'file1.json'
bad_conf_path = 'file2.json'


with open(good_count_path, 'r', encoding='utf-8') as file1:
    good_count = json.load(file1)

with open(good_conf_path, 'r', encoding='utf-8') as file1:
    good_conf = json.load(file1)

with open(good_count_path, 'r', encoding='utf-8') as file1:
    bad_count = json.load(file1)

with open(good_conf_path, 'r', encoding='utf-8') as file1:
    bad_conf = json.load(file1)



# # 示例数据

data = bad_count

# 创建直方图
plt.hist(data, bins=5, alpha=0.7, color='blue', edgecolor='black')

# 添加标题和标签
plt.title('示例直方图')
plt.xlabel('值')
plt.ylabel('frequency')

# 显示图形
plt.show()
import json
import matplotlib.pyplot as plt

dir = "liutao_cn"
file_prefix = "liutao_chinses_r0.7_Filtered_img_confidence"
ids = range(10,30)


total_dir = {}

for id in ids:
    file_path = dir + "/" + file_prefix + str(id) + ".json"

    with open(file_path, 'r', encoding='utf-8') as file1:
        good_conf = json.load(file1)
    for key in good_conf.keys():
        total_dir[key] = good_conf[key]

print(len(total_dir))

conf = total_dir
# # 示例数据

counts = []
avg_conf = []
#

conf_0 = 0
conf_non_zero = 0

for key in conf:
    conf_list = conf[key]
    count = len(conf_list)
    if count>=0:
        counts.append(count)
        if count == 0:
            avg_conf.append(0)
            conf_0 +=1
        else:
            avg_conf.append(sum(conf_list) / count)
            conf_non_zero += 1

#
plt.plot(counts, avg_conf,"o")
# 添加标题和标签
plt.title('confidence vs frame count ')
plt.xlabel('hand frame detected (per video)')
plt.ylabel('average confidence')

# 显示图形
plt.show()


plt.hist(counts, bins=20, alpha=0.7, color='blue', edgecolor='black')

# 添加标题和标签
plt.title('hand prediction frame count')
plt.xlabel('hand frame detected (per video)')
plt.ylabel('sample frequency')
# 显示图形
plt.show()

print(conf_0, conf_non_zero)
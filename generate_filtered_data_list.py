import json
import matplotlib.pyplot as plt


conf_path = 'G:/hand_detect/hand_object_detector/results_v2/tecent_img_confidence0.json'
out_path = 'G:/hand_detect/hand_object_detector/results_v2/tecent_hand_list.json'


with open(conf_path, 'r', encoding='utf-8') as file1:
    conf = json.load(file1)





# # 示例数据

counts = []
avg_conf = []
#
for key in conf:
    conf_list = conf[key]
    count = len(conf_list)
    if count<100:
        counts.append(count)
        if count == 0:
            avg_conf.append(0)
        else:
            avg_conf.append(sum(conf_list) / count)

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


out_put = []
#
conf_thresholds = [0.8]
count_thresholds = [200]

for conf_th in conf_thresholds:
    for count_th in count_thresholds:
        # count hand data, positive data
        for key in conf:
            conf_list = conf[key]
            count = len(conf_list)
            if count == 0:
                avg_conf = 0
            else:
                avg_conf = sum(conf_list) / count

            if avg_conf >= conf_th or count >= count_th:
                #  predict positive
                out_put.append(key)
            else:
                # predict negative
                continue


print(out_put)
#

with open(out_path, 'w', encoding='utf-8') as file:
    # 将字典转换为json格式并写入文件
    json.dump(out_put, file, ensure_ascii=False, indent=4)








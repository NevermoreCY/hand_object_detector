import json
import matplotlib.pyplot as plt

good_count_path = 'G:/hand_detect/hand_object_detector/results/bili_good_img_count.json'
good_conf_path = 'G:/hand_detect/hand_object_detector/results/bili_good_img_confidence.json'
bad_count_path = 'G:/hand_detect/hand_object_detector/results/bili_bad_img_count0.json'
bad_conf_path = "G:/hand_detect/hand_object_detector/results/bili_bad_img_confidence0.json"


with open(good_count_path, 'r', encoding='utf-8') as file1:
    good_count = json.load(file1)

with open(good_conf_path, 'r', encoding='utf-8') as file1:
    good_conf = json.load(file1)

with open(bad_count_path, 'r', encoding='utf-8') as file1:
    bad_count = json.load(file1)

with open(bad_conf_path, 'r', encoding='utf-8') as file1:
    bad_conf = json.load(file1)



# # 示例数据

# counts = []
# avg_conf = []
#
# for key in good_conf:
#     conf_list = good_conf[key]
#     count = len(conf_list)
#
#     if count>=0:
#         counts.append(count)
#         if count == 0:
#             avg_conf.append(0)
#         else:
#             avg_conf.append(sum(conf_list) / count)

#
# plt.plot(counts, avg_conf,"o",label="No Hand" )
# # 添加标题和标签
# plt.title('confidence vs frame count for bili Non-hand samples')
# plt.xlabel('hand frame detected (per video)')
# plt.ylabel('average confidence')
#
# # 显示图形
# plt.show()


# plt.hist(counts, bins=20, alpha=0.7, color='blue', edgecolor='black')

# # 添加标题和标签
# plt.title('hand prediction frame count for bili Non-hand samples')
# plt.xlabel('hand frame detected (per video)')
# plt.ylabel('sample frequency')
# # 显示图形
# plt.show()




# counts = []
# for key in bad_count:
#     if bad_count[key] < 100:
#         counts.append(bad_count[key])
#
# print(len(counts))
# # 创建直方图
# plt.hist(counts, bins=10, alpha=0.7, color='blue', edgecolor='black')
#
# # 添加标题和标签
# plt.title('hand prediction frame count for bili Non-hand samples')
# plt.xlabel('hand frame detected (per video)')
# plt.ylabel('sample frequency')
#
# # 显示图形
# plt.show()
#
# plt.hist(avg_conf, bins=20, alpha=0.7, color='blue', edgecolor='black')
#
# # 添加标题和标签
# plt.title('average confidence for bili Non-hand samples')
# plt.xlabel('average confidence  (per video)')
# plt.ylabel('sample frequency')

# 显示图形
# plt.show()
#
#
# counts = []
# avg_conf = []
#
# for key in bad_conf:
#     conf_list = bad_conf[key]
#     count = len(conf_list)
#
#     if count>=0:
#         counts.append(count)
#         if count == 0:
#             avg_conf.append(0)
#         else:
#             avg_conf.append(sum(conf_list) / count)
# #
#
# plt.plot(counts, avg_conf,"o" ,color = 'r',label="With Hand")
#
# # 添加标题和标签
# plt.title('confidence vs frame count range all')
# plt.xlabel('hand frame detected (per video)')
# plt.ylabel('average confidence')
# plt.legend()
# # 显示图形
# plt.show()


# plt.hist(counts, bins=20, alpha=0.7, color='blue', edgecolor='black')
#
# # 添加标题和标签
# plt.title('hand prediction frame count for bili hand samples')
# plt.xlabel('hand frame detected (per video)')
# plt.ylabel('sample frequency')
#
# # 显示图形
# plt.show()

# plt.hist(avg_conf, bins=20, alpha=0.7, color='blue', edgecolor='black')
#
# # 添加标题和标签
# plt.title('average confidence for bili hand samples')
# plt.xlabel('average confidence  (per video)')
# plt.ylabel('sample frequency')
#
# # 显示图形
# plt.show()
# Grid search

tp = 0
tn = 0
fp = 0
fn = 0
#
out_dir = []

conf_thresholds = [0.85,0.8,0.75,0.7,0.65]
count_thresholds = [200,250,300]

for conf_th in conf_thresholds:
    for count_th in count_thresholds:
        # count hand data, positive data
        for key in bad_conf:
            conf_list = bad_conf[key]
            count = len(conf_list)
            if count == 0:
                avg_conf = 0
            else:
                avg_conf = sum(conf_list) / count

            if avg_conf >= conf_th or count >= count_th:
                #  predict positive
                tp += 1
            else:
                # predict negative
                fn +=1
        # check data without hand ; negative data
        for key in good_conf:
            conf_list = good_conf[key]
            count = len(conf_list)
            if count == 0:
                avg_conf = 0
            else:
                avg_conf = sum(conf_list) / count

            if avg_conf >= conf_th or count >= count_th:
                #  predict positive
                fp += 1
            else:
                # predict negative
                tn +=1
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        to_save = [count_th,conf_th,precision,recall,tn,fp,fn,fp]
        print(to_save)
        out_dir.append(to_save)

print(out_dir)











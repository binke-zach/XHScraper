import json
import datetime

# 读取JSON文件中的评论数据
with open('..\\MediaCrawler\\data\\xhs\\json\\search_comments_2024-12-30.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

# 按like_count降序排序，注意like_count是字符串类型，需要先转为整数进行排序
# sorted_comments = sorted(comments, key=lambda x: int(x['like_count']), reverse=True)

# 获取前10条评论
# top_10_comments = sorted_comments[:10]

# 对每条评论的create_time进行转换
filtered_comments = []

for comment in comments:
    # 转换create_time时间戳（毫秒）为秒
    timestamp = int(comment['create_time']) / 1000  # 毫秒转为秒
    dt_object = datetime.datetime.utcfromtimestamp(timestamp)  # 转为UTC时间
    
    # 转换为中国标准时间（CST，UTC+8）
    china_time = dt_object + datetime.timedelta(hours=8)
    
    # 只保留2024年的评论
    if china_time.year == 2024:
        # 提取中国标准时间的月份（使用整数格式）
        comment['create_month'] = china_time.month  # 直接取月份
        filtered_comments.append(comment)
    else:
        comment['create_month'] = 0
        filtered_comments.append(comment)

# 输出过滤后的评论
for comment in filtered_comments:
    print(f"评论ID: {comment['comment_id']} - 创建时间: {china_time} - 月份: {comment['create_month']}")

# 如果需要保存结果为新文件，可以使用以下代码：
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_comments, f, ensure_ascii=False, indent=4)

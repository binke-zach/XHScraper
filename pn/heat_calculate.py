import json
import math
from datetime import datetime

# 读取JSON文件中的帖子数据
def load_contents_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = json.load(f)
    return contents

# 计算热度
def calculate_hotness(post):
    # 将数值字段从字符串转换为整数
    liked_count = float(post['liked_count'].replace('万', '')) * 10000 if '万' in post['liked_count'] else int(post['liked_count'])
    collected_count = float(post['collected_count'].replace('万', '')) * 10000 if '万' in post['collected_count'] else int(post['collected_count'])
    comment_count = float(post['comment_count'].replace('万', '')) * 10000 if '万' in post['comment_count'] else int(post['comment_count'])
    share_count = float(post['share_count'].replace('万', '')) * 10000 if '万' in post['share_count'] else int(post['share_count'])

    # 假设系数
    like_weight = 0.25
    collect_weight = 0.3
    comment_weight = 0.25
    share_weight = 0.02  
    alpha = 0.001  # 转发按指数增长
    
    # 限制指数增长，防止溢出
    max_share_exp = 1000  # 最大的指数值
    share_count_exp = min(share_count, max_share_exp)  # 限制最大值
    share_count_exp = math.exp(alpha * share_count_exp)  # 计算指数值

    # 基础热度计算
    hotness = (liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + math.exp(alpha * share_count) * share_weight)

    return hotness

# 计算每个帖子的热度并排序
def process_posts(posts):
    post_hotness = []
    
    for post in posts:
        hotness = calculate_hotness(post)
        post_hotness.append({
            'note_id': post['note_id'],
            'title': post['title'],
            'hotness': hotness,
            'city': "shanghai"
            # 'last_update_time': timestamp_to_date(post['last_update_time']),
            # 'note_url': post['note_url']
        })
    
    # 按热度降序排列
    post_hotness_sorted = sorted(post_hotness, key=lambda x: x['hotness'], reverse=True)
    
    return post_hotness_sorted




if __name__ == "__main__":
    file_path = "shanghai_search_contents_2024-12-24.json"

    posts = load_contents_data(file_path)

    # 输出计算后的热度排名
    posts_hotness = process_posts(posts)

    for post in posts_hotness:
        print(f"Note ID: {post['note_id']} | Title: {post['title']} | Hotness: {post['hotness']}" )

    # 如果需要保存结果为新文件，可以使用以下代码：
    with open('shanghai_heat_2024.json', 'w', encoding='utf-8') as f:
        json.dump(posts_hotness, f, ensure_ascii=False, indent=4)
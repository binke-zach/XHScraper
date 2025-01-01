import json
import math
from datetime import datetime

# 读取JSON文件中的帖子数据
def load_contents_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = json.load(f)
    return contents

#字符处理函数
def clean_count(count_str):
    # 去掉非数字字符（'万', '千', '+' 等）
    count_str = count_str.replace('万', '').replace('千', '').replace('+', '').strip()
    
    try:
        # 判断字段是否包含 '万' 或 '千'，并进行相应的转换
        if '万' in count_str:
            return float(count_str) * 10000  # 万 -> 10000
        elif '千' in count_str:
            return float(count_str) * 1000   # 千 -> 1000
        else:
            return int(count_str)  # 如果没有单位，直接转换为整数
    except ValueError:
        # 如果转换失败，返回 0 或其他默认值
        return 0


# 计算热度
def calculate_hotness(post):
    # 将数值字段从字符串转换为整数
    liked_count = clean_count(post['liked_count'])
    collected_count = clean_count(post['collected_count'])
    comment_count = clean_count(post['comment_count'])
    share_count = clean_count(post['share_count'])
    # 假设系数
    like_weight = 0.3
    collect_weight = 0.3
    comment_weight = 0.2
    share_weight = 0.2
    alpha = 0.001  # 转发按指数增长
    
    if share_count <= 8000:
        hotness = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_count * share_weight 
    elif share_count <= 10000:
        hotness1 = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_count * share_weight
        hotness2 = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_weight * math.exp(alpha * share_count)
        hotness = max(hotness1, hotness2)
    elif share_count <= 12000:
        hotness2 = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_weight * math.exp(alpha * share_count)
        hotness3 = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_count * share_weight + 5000
        hotness = max(hotness2, hotness3)
    else:
        hotness = liked_count * like_weight + collected_count * collect_weight + comment_count * comment_weight + share_count * share_weight + 5000
     
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
    file_path = "..\\MediaCrawler\\data\\xhs\\json\\search_contents_2024-12-30.json"

    posts = load_contents_data(file_path)

    # 输出计算后的热度排名
    posts_hotness = process_posts(posts)

    for post in posts_hotness:
        print(f"Note ID: {post['note_id']} | Title: {post['title']} | Hotness: {post['hotness']}" )

    # 如果需要保存结果为新文件，可以使用以下代码：
    with open('data2.json', 'w', encoding='utf-8') as f:
        json.dump(posts_hotness, f, ensure_ascii=False, indent=4)
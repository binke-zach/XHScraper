import json

# 读取 JSON 文件
with open('..\\MediaCrawler\\data\\xhs\\json\\search_contents_2025-01-02.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历每条记录，合并字段，并删除原字段
for record in data:
    # 合并字段
    record['text'] = record['title'] + record['desc'] + record['tag_list']  # 或者使用其他合并方式

    # 删除原有的字段
    del record['note_id']
    del record['type']
    del record['video_url']
    del record['time']
    del record['last_update_time']
    del record['user_id']
    del record['nickname']
    del record['avatar']
    del record['liked_count']
    del record['collected_count']
    del record['comment_count']
    del record['share_count']
    del record['ip_location']
    del record['image_list']
    del record['source_keyword']
    del record['last_modify_ts']
    del record['note_url']
    del record['xsec_token']
    del record['title']
    del record['desc']
    del record['tag_list']

# 将修改后的数据写回文件，只保留 merged_field 字段
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 打印合并后的数据
print(json.dumps(data, ensure_ascii=False, indent=4))

import json

# 读取JSON文件中的数据
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 将评论按每5条归属到帖子中
def add_comments_to_posts(posts, comments):
    for i, post in enumerate(posts):
        # 获取该帖子的评论，假设评论按顺序存储，每5条归属到一个帖子
        post_comments = comments[i*5:(i+1)*5]
        
        # 获取每条评论的comment_id和create_month
        comments_info = [{'comment_id': comment['comment_id'], 'create_month': comment['create_month']} for comment in post_comments]
        
        # 将评论信息添加到帖子的字典中
        post['comments'] = comments_info
    
    return posts

# 保存修改后的JSON数据到文件
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 主程序
if __name__ == "__main__":
    # 文件路径
    posts_file = 'data2.json'  # 帖子数据文件
    comments_file = 'data1.json'  # 评论数据文件
    output_file = 'result.json'  # 输出文件

    # 加载数据
    posts = load_json(posts_file)
    comments = load_json(comments_file)

    # 将评论信息添加到帖子中
    updated_posts = add_comments_to_posts(posts, comments)

    # 保存修改后的帖子数据
    save_json(output_file, updated_posts)

    print(f"修改后的帖子数据已保存到 {output_file}")

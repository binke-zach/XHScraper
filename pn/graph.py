import json
import matplotlib.pyplot as plt
import numpy as np

# 读取JSON文件中的数据
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 根据评论月份分配热度到对应月份
def distribute_hotness(post, comments):
    # 计算每条评论的热度分配
    monthly_hotness = {month: 0 for month in range(1, 13)}  # 存储1-12月的热度
    
    # 获取帖子的总热度
    post_hotness = post['hotness']
    
    # 获取评论的月份和分配热度
    valid_comments = [comment for comment in comments if comment['create_month'] != 0]
    
    # 分配热度到对应的月份
    for comment in valid_comments:
        month = comment['create_month']
        monthly_hotness[month] += post_hotness / 5  # 每条评论分配1/5的热度

    return monthly_hotness

# 汇总每个城市的热度数据
def get_city_heatmap(cities_data):
    city_monthly_hotness = {}
    
    for city in cities_data:
        city_name = city['city']  # 获取城市名称

        # 如果没有这个城市，初始化该城市每个月的热度
        if city_name not in city_monthly_hotness:
            city_monthly_hotness[city_name] = {month: 0 for month in range(1, 13)}
        
        # city_heatmap = {month: 0 for month in range(1, 13)}  # 存储1-12月的总热度
        
        # 遍历每个帖子的评论并分配热度       
        comments = city['comments']  # 每个帖子有5条评论
        monthly_hotness = distribute_hotness(city, comments)
        
        # 汇总该帖子的热度到各个月份
        for month, hotness in monthly_hotness.items():
            city_monthly_hotness[city_name][month] += hotness
        #     city_heatmap[month] += hotness
        
        # hot = city_monthly_hotness[city_name]
        # for month, hotness in hot.items():
        #     hot[month] += city_heatmap[month]
        # print(city_monthly_hotness[])
    
    return city_monthly_hotness

# 绘制热度折线图并保存为文件
def plot_heatmap(city_monthly_hotness, output_file='heatmap.png'):
    months = np.arange(1, 13)
    
    for city, monthly_hotness in city_monthly_hotness.items():
        heat_values = [monthly_hotness[month] for month in months]
        
        # 绘制折线图
        plt.plot(months, heat_values, label=city)

    plt.xlabel('Month')
    plt.ylabel('Heat')
    plt.title('2024 Travel City Heat Over Months')
    plt.xticks(months)  # 设置横轴为1到12月份
    plt.legend()  # 显示城市的图例
    plt.grid(True)
    
    # 保存图像到文件
    plt.savefig(output_file, dpi=300)  # 保存为文件，设置300dpi提高图像质量
    print(f"Heatmap saved to {output_file}")
    
    # 显示图像
    plt.show()

# 主程序
if __name__ == "__main__":
    # 假设数据已经加载为字典，包含10个城市，每个城市有20个帖子
    cities_file = 'shanghai_together.json'  # 含有10个城市的数据文件
    cities_data = load_json(cities_file)

    # print(cities_data)

    # 获取每个城市的热度数据
    city_monthly_hotness = get_city_heatmap(cities_data)

    # 保存热度折线图
    plot_heatmap(city_monthly_hotness, output_file='city_heatmap_2024.png')
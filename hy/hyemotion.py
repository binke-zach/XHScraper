import json
import matplotlib.pyplot as plt
from cnsenti import Emotion
import seaborn as sns


# 加载JSON文件
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# 情绪词统计和分类
def classify_emotion(text, emotion_analyzer):
    result = emotion_analyzer.emotion_count(text)

    # 直接过滤掉 'words' 和 'sentences'，只考虑情绪词
    valid_emotions = {key: value for key, value in result.items() if key not in ['words', 'sentences']}

    # 找到出现次数最多的情绪
    max_emotion = max(valid_emotions, key=valid_emotions.get)

    return max_emotion


# 统计每种情绪的文本数量
def emotion_distribution(mblogs, emotion_analyzer):
    emotion_count = {
        '乐': 0,
        '哀': 0,
        '怒': 0,
        '惧': 0,
        '恶': 0,
        '惊': 0,
        '无情绪': 0
    }

    for blog in mblogs:
        text = blog.get('text', '')
        emotion = classify_emotion(text, emotion_analyzer)
        if emotion in emotion_count:
            emotion_count[emotion] += 1
        else:
            emotion_count['无情绪'] += 1

    return emotion_count


# 绘制条形图
def plot_bar_chart(emotion_count, save_path):
    # 提取标签和对应的数量
    labels = list(emotion_count.keys())
    sizes = list(emotion_count.values())

    # 计算比例
    total = sum(sizes)
    proportions = [size / total * 100 for size in sizes]

    sns.set_style('whitegrid')
    custom_colors = sns.color_palette("BrBG_r")

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示设置
    plt.rcParams['axes.unicode_minus'] = False
    # 创建条形图
    plt.figure(figsize=(10, 6))
    plt.barh(labels, proportions, color=custom_colors)

    # 设置标题和标签
    plt.title('帖子情绪倾向统计图')
    plt.xlabel('比例 (%)')
    plt.ylabel('情绪类别')

    # 显示比例在条形上
    for i, v in enumerate(proportions):
        plt.text(v + 1, i, f'{v:.1f}%', color='black', va='center', fontweight='bold')

    custom_labels = ['快乐', '悲伤', '愤怒', '恐惧', '厌恶', '惊讶', '平和']
    plt.yticks(labels, custom_labels)

    # 保存图像为png文件
    plt.savefig(save_path, format='png', dpi=300)  # 设置文件路径和dpi
    print(f"图像已保存为 {save_path}")
    
    # 显示图表
    


if __name__ == '__main__':
    # 加载情绪分析器
    emotion_analyzer = Emotion()

    # 读取JSON文件，假设文件名为 'data.json'
    filename = 'data.json'  # 你可以替换成你自己的文件名
    mblogs = load_json(filename)

    print('微博总数：', len(mblogs))

    # 统计情绪分类
    emotion_count = emotion_distribution(mblogs, emotion_analyzer)
    print('情绪分布：', emotion_count)

    # 保存图像文件路径
    save_path = '2emotion.png'  # 你可以修改成你想保存的路径

    # 绘制条形图并保存为png文件
    plot_bar_chart(emotion_count, save_path)


import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = ""
SECRET_KEY = ""

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    response = requests.post(url, params=params)
    return response.json().get("access_token")


def analyze_sentiment(text, access_token):
    """
    使用百度的情感分析API分析文本的情感倾向
    :param text: 需要分析的文本
    :param access_token: 通过 get_access_token() 获取的 Access Token
    :return: 情感分析的结果（positive、negative 或 neutral）
    """
    url = f"https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={access_token}"

    payload = json.dumps({"text": text})  # 将文本包装成JSON格式
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    result = response.json()

    if "items" in result:
        sentiment = result["items"][0]["sentiment"]
        if sentiment == 2:
            return "positive"
        elif sentiment == 0:
            return "negative"
        else:
            return "neutral"
    else:
        print(f"Error analyzing text: {text}")
        return None


def main():
    # 获取access_token
    access_token = get_access_token()

    if not access_token:
        print("无法获取 access_token，请检查API密钥。")
        return

    # 读取JSON文件
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 初始化情感计数器
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

    # 遍历每条记录，分析情感
    for item in data:
        text = item.get("text")  # 获取文本字段
        if text:
            sentiment = analyze_sentiment(text, access_token)
            if sentiment:
                sentiment_counts[sentiment] += 1

    # 输出情感数量
    print(f"积极情感数量: {sentiment_counts['positive']}")
    print(f"消极情感数量: {sentiment_counts['negative']}")
    print(f"中立情感数量: {sentiment_counts['neutral']}")

    # 计算情感占比
    total_count = sum(sentiment_counts.values())
    percentages = [sentiment_counts["negative"] / total_count,
                   sentiment_counts["neutral"] / total_count,
                   sentiment_counts["positive"] / total_count]

    # 情绪标签
    labels = ['消极', '中性', '积极']

    # 设置颜色（根据情绪类型）
    sns.set_style('whitegrid')
    custom_colors = sns.color_palette("BrBG_r")
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 绘制饼状图
    plt.pie(percentages, labels=labels, colors=custom_colors, autopct='%1.1f%%', startangle=90)

    # 添加标题
    plt.title('情感分析')

    # 保存图像为png文件
    save_path = '3emotion.png'  # 保存的文件路径
    plt.savefig(save_path, format='png', dpi=300)  # 保存图像，设置高分辨率
    print(f"图像已保存为 {save_path}")

    # 显示图形
    plt.show()


if __name__ == '__main__':
    main()


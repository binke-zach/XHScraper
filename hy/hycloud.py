# coding: utf-8

import json
import jieba.analyse
import matplotlib as mpl
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def keywords(mblogs, ignore_words=None):
    # 如果忽略词列表为空，设置默认值为空集合
    if ignore_words is None:
        ignore_words = set()

    text = []
    for blog in mblogs:
        # 提取关键词
        keyword = jieba.analyse.extract_tags(blog['text'])
        # 移除忽略的词
        filtered_keywords = [word for word in keyword if word not in ignore_words]
        print(filtered_keywords)
        text.extend(filtered_keywords)
    return text


def gen_img(texts, img_file):
    # 使用集合去重，避免重复词出现
    # unique_words = set(texts)
    # data = ' '.join(text for text in unique_words)
    data = ' '.join(text for text in texts)
    # 配置词云生成
    wc = WordCloud(
        background_color='white',
        scale=4,
        repeat=False,
        collocations=False,
        font_path='C:/Windows/Fonts/simhei.ttf'
    )
    wc.generate(data)

    # 保存图片
    wc.to_file(img_file.split('.')[0] + '_wc.png')


if __name__ == '__main__':
    filename = 'data.json'

    # 从文件加载微博数据
    with open(filename, 'r', encoding='utf-8') as file:
        mblogs = json.load(file)

    print('微博总数：', len(mblogs))

    # 定义要忽略的关键词，可以根据需要添加更多关键词
    ignore_words = {'话题'}

    # 提取关键词，并过滤掉忽略的词
    words = keywords(mblogs, ignore_words)
    print("总词数：", len(words))

    # 生成词云并保存
    gen_img(words, '1cloud.png')

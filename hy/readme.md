# 代码简介
## hysort.py:
```python
with open('search_contents_2024-12-23.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
```
其中search_contents_2024-12-23.json是原爬虫结果的json文件。此代码用于将爬虫结果的json文件通过删除和合并字段生成用于分析的data.json。
## hycloud.py
此代码用于产生讨论词云，输入为data.json，输出为png文件1cloud.png。
## hyemotion.py
此代码用于产生情感分类分析条形图，输入为data.json，输出为png文件2emotion.png。
## hyapi.py
此代码用于产生情感倾向分析饼状图，输入为data.json，输出为png文件3emotion.png。

## 整体使用
将爬虫得到的json文件名放入hysort.py代码，之后先运行hysort.py，结束后依次或同时运行剩下三个py文件即可。
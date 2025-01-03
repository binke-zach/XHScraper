# scraper/views.py
import os
import subprocess
import shutil
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import KeywordForm, IDForm  # 引入 IDForm

def move_images_to_media():
    """
    将 hy 和 pn 文件夹下的生成图片移动到 media 文件夹中
    """
    # hy 目录下的图片
    hy_image_files = ['1cloud_wc.png', '2emotion.png', '3emotion.png']
    pn_image_files = ['heatmap.png']

    # 构建图片源路径和目标路径
    for image in hy_image_files + pn_image_files:
        # 生成源路径
        src_path = os.path.join(settings.BASE_DIR, 'hy' if image in hy_image_files else 'pn', image)
        # 生成目标路径
        dst_path = os.path.join(settings.MEDIA_ROOT, image)

        # 如果文件存在，移动到 media 目录
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path)

def run_scraper(keyword=None, user_id=None, search_type="search"):
    """
    运行爬虫程序，依次调用相关的 Python 脚本
    """
    # 判断是根据关键词还是 ID 来运行爬虫
    if user_id:
        command = f"python main.py --type creator --id {user_id}"
    elif keyword:
        command = f"python main.py --type search --keywords {keyword}"
    else:
        raise ValueError("No valid input provided for keyword or ID")

    # 运行 main.py 脚本
    subprocess.run(command, shell=True, cwd=os.path.join(settings.BASE_DIR, 'MediaCrawler'))

    # 运行 hy 目录下的脚本
    hy_scripts = [
        'hysort.py', 'hycloud.py', 'hyemotion.py', 'hyapi.py'
    ]
    for script in hy_scripts:
        subprocess.run(f"python {script}", shell=True, cwd=os.path.join(settings.BASE_DIR, 'hy'))

    # 运行 pn 目录下的脚本
    pn_scripts = [
        'time_format.py', 'heat_calculate.py', 'together.py', 'graph.py'
    ]
    for script in pn_scripts:
        subprocess.run(f"python {script}", shell=True, cwd=os.path.join(settings.BASE_DIR, 'pn'))
        
    move_images_to_media()

    # 返回生成的图片路径
    return [
        os.path.join(settings.MEDIA_URL, '1cloud_wc.png'),
        os.path.join(settings.MEDIA_URL, '2emotion.png'),
        os.path.join(settings.MEDIA_URL, '3emotion.png'),
        os.path.join(settings.MEDIA_URL, 'heatmap.png')
    ]

def index(request):
    """
    展示关键词/ID输入页面
    """
    if request.method == 'POST':
        # 判断是提交关键词还是ID
        if 'keyword' in request.POST:
            form = KeywordForm(request.POST)
            if form.is_valid():
                keyword = form.cleaned_data['keyword']
                image_paths = run_scraper(keyword=keyword)  # 按关键词运行爬虫
                return render(request, 'scraper/results.html', {'images': image_paths, 'keyword': keyword})
        elif 'id' in request.POST:
            form = IDForm(request.POST)
            if form.is_valid():
                user_id = form.cleaned_data['id']
                image_paths = run_scraper(user_id=user_id, search_type="creator")  # 按 ID 运行爬虫
                return render(request, 'scraper/results.html', {'images': image_paths, 'user_id': user_id})

    else:
        form = KeywordForm()

    return render(request, 'scraper/index.html', {'form': form})

def results(request):
    """
    展示爬虫运行结果及生成的图片
    """
    images = [
        '1cloud_wc.png',
        '2emotion.png',
        '3emotion.png',
        'heatmap.png',
    ]
    image_paths = [os.path.join(settings.MEDIA_URL, image) for image in images]
    return render(request, 'scraper/results.html', {'image_paths': image_paths})
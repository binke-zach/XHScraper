from django.shortcuts import render
from django.http import HttpResponse
from .forms import ScraperForm
from .models import ScraperTask
import os
from subprocess import Popen, PIPE  # 用于调用外部爬虫脚本

def scraper_view(request):
    if request.method == 'POST':
        form = ScraperForm(request.POST)
        if form.is_valid():
            # 获取表单数据
            keyword = form.cleaned_data['keyword']
            xhs_id = form.cleaned_data['xhs_id']

            # 假设爬虫程序是一个 Python 脚本，调用爬虫程序并获取图片
            # 示例：调用爬虫并传递参数，返回图片路径
            result_image_path = run_scraper(keyword, xhs_id)

            # 保存爬取结果到数据库
            task = ScraperTask.objects.create(
                keyword=keyword,
                xhs_id=xhs_id,
                result_image=result_image_path
            )

            return render(request, 'scraper/result.html', {'task': task})
    else:
        form = ScraperForm()

    return render(request, 'scraper/index.html', {'form': form})

def run_scraper(keyword, xhs_id):
    # 这里调用爬虫程序，传入参数并获取生成的 PNG 图片
    # 例如，我们调用一个外部 Python 脚本来执行爬取，并将结果存储为图片
    # Popen 用于启动外部进程
    command = f"python3 /path/to/your/scraper_script.py --keyword {keyword} --id {xhs_id}"
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # 假设脚本返回的图片文件存储在 /path/to/save/result.png
    # 返回文件路径
    return "/media/scraper_results/result.png"

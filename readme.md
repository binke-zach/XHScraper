# 小红书爬虫程序环境配置与运行
```shell
# 运行前在hy\hyapi.py的下列代码处配置自己的api：

API_KEY = ""
SECRET_KEY = ""
```
# 创建并激活 python 虚拟环境
   ```shell   
   # 进入项目根目录
   # 创建虚拟环境
   # python版本是：3.9.6，新版本的Python可能会出现库依赖不兼容问题：requirements.txt
   py -3.9 -m venv venv
   
   # macos & linux 激活虚拟环境
   source venv/bin/activate

   # windows 激活虚拟环境
   venv\Scripts\activate

   ```

## 安装依赖库

   ```shell
   pip install -r requirements.txt
   ```

## 安装 playwright浏览器驱动

   ```shell
   playwright install
   ```

## 运行爬虫程序
    ```shell
   cd xhs_project
   python manage.py migrate
   python manage.py runserver
   ```
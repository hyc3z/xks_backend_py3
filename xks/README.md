# xks-server

### 使用虚拟环境，并下载相关库
```
cd 后端_Python/
source datavis/bin/activate
cd xks
pip3 freeze > requirements.txt 
```

### 基本操作（可参考官网）
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
[服务器网页](http://127.0.0.1:8000/).
[服务器管理网页](http://127.0.0.1:8000/admin/).

### 参考
[Django官网](https://docs.djangoproject.com/zh-hans/).
[restframework官网](https://www.django-rest-framework.org/).
一定要使用requirements里面版本的库，不然会有很多奇怪的bug.

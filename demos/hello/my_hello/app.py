# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/18 下午7:34
# @Author    : ABC
# @FileName  : app.py
from flask import Flask

app = Flask(__name__)


# 可以同时为视图函数绑定多个路由
@app.route('/hi')
@app.route('/hello')
@app.route('/')  # route()装饰器接受的第一个参数为字符串且必须以`/`开头
def index():
    return '<h1>Hello Flask!</h1>'


# defaults参数设置URL变量的默认值，接受字典类型参数，存储URL变量和默认值的映射
@app.route('/greet/', defaults={'name': "Programmer"})
@app.route('/greet/<name>')  # 在URL规则中添加变量<name>
def greet(name):
    return f'<h1>Hello {name}!</h1>'


'''
1.可以在app程序实例的当前目录下使用`flask run`方法启动服务器
2.使用app.run()方法属于旧的启动开发服务器的方法，目前已不推荐使用。
'''
if __name__ == '__main__':
    app.run(debug=True)

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/19 下午12:27
# @Author    : ABC
# @FileName  : hello.py
import click
from flask import Flask, url_for

app = Flask(__name__)

'''
添加单个配置项
最好在程序实例app创建后就加载配置
'''
# app.config['DEBUG'] = True
'''
添加多个配置项
'''
# app.config.update(
#     TESTING=True,
#     SECRET_KEY='fc31f95e553f48e5ac0c71161ee95239'
# )

'''
读取配置项的值
'''


# value1 = app.config.get('TESTING')
# value2 = app.config['SECRET_KEY']


# 可以同时为视图函数绑定多个路由
@app.route('/hi')
@app.route('/hello')
@app.route('/')  # route()装饰器接受的第一个参数为字符串且必须以`/`开头
def index():
    return '<h4>Hello Flask!</h4>'


# defaults参数设置URL变量的默认值，接受字典类型参数，存储URL变量和默认值的映射
@app.route('/greet/', defaults={'name': "Programmer"})
@app.route('/greet/<name>')  # 在URL规则中添加变量<name>
def greet(name):
    return f'<h1>Hello {name}!</h1>'


@app.route('/admin')
def admin():
    # 调用url_for('admin')获取对应的URL，即`/admin`(获取到的是URL的相对路径)
    # url_for()第一个参数为端点值(在flask中,端点用来标记一个视图函数以及对应的URL规则，端点的默认值为视图函数名称)
    print("url_for('admin'):", url_for('admin'))
    # 在url_for()函数里通过设置`_external=True`来获取URL的绝对路径，即`http://127.0.0.1:5000/admin`
    print("url_for('admin', _external=True):", url_for('admin', _external=True))
    return '<h4>this page is for admin user!</h4>'


@app.route('/user/<username>')
def user(username):
    # 调用url_for()获取对应的URL
    # url_for()第一个参数为端点值(在flask中,端点用来标记一个视图函数以及对应的URL规则，端点的默认值为视图函数名称)
    # 如果URL含有动态部分，需要在url_for()函数中传入相应的参数
    print("url_for('user', username='Jack'):", url_for('user', username='Jack'))
    return f'<h4>hello {username}!</h4>'


'''
any转换器的使用:事先定义好可以传入的值。当访问定义好的值之外的值时，会报404错误
'''
# @app.route('/colors/<any(blue, red, green):color>')
# def colors(color):
#     return f'current color is {color}'

colors = ['blue', 'red', 'green']


@app.route(f'/colors/<any({str(colors)[1:-1]}):color>')
def colors(color):
    return f'current color is {color}'


# 通过`@app.cli.command()`装饰器可以注册一个flask命令
# 函数的名称即为命令名称，这里注册的命令即`hello`，即可以使用`flask hello`命令来触发该函数
@app.cli.command()
def hello():
    # 下边是文档字符串，当在执行`flask hello --help`命令时会作为帮助信息展示出来
    '''命令行文档注释示例:Just say hello!'''
    click.echo('Hello Human!')


# 通过`@app.cli.command()`装饰器可以注册一个flask命令
# 函数的名称即为命令名称，这里注册的命令即`hello`，即可以使用`flask hello`命令来触发该函数
# 也可以通过在装饰器`@app.cli.command()`中传入参数来设置命令名称，如：@app.cli.command('hello-custom-name')会把命令名称设置为`hello-custom-name`,完整命令即`flask hello-custom-name`
@app.cli.command('hello-custom-name')
def hello_custom_command_name():
    # 下边是文档字符串，当在执行`flask hello --help`命令时会作为帮助信息展示出来
    '''命令行文档注释示例(自定义命令名称):Just say hello!'''
    click.echo('hello_custom_command_name >>> Hello Human!')


'''
1.可以在app程序实例的当前目录下使用`flask run`方法启动服务器
2.使用app.run()方法属于旧的启动开发服务器的方法，目前已不推荐使用。
'''
if __name__ == '__main__':
    app.run(debug=True)

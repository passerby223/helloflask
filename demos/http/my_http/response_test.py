#!/usr/bin/python3
# @FileName    :response_test.py
# @Time        :2020/6/21 下午6:13
# @Author      :ABC
# @Description :
import os
from flask import Flask, make_response, redirect, url_for, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret_key')

@app.route('/')
def foo():
    # 通过请求对象获取cookie
    cookie_name = request.cookies.get('name')
    res = make_response(f'<h1>hello world!</h1> cookie_name: {cookie_name}')
    # 手动设置响应体的MIME类型
    res.mimetype = 'text/plain'
    # 手动设置响应头的content-type属性
    res.headers['Content-Type'] = 'text/plain;charset=utf-8'
    return res

# 手动在响应中添加cookie
@app.route('/set/<cookie_name>')
def set_cookie(cookie_name):
    res = make_response(redirect(url_for('foo')))
    res.set_cookie('name', cookie_name)
    return res


if __name__ == '__main__':
    app.run(debug=True)

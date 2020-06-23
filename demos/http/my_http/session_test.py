#!/usr/bin/python3
# @FileName    :session_test.py
# @Time        :2020/6/21 下午7:42
# @Author      :ABC
# @Description :
import os
from flask import Flask, make_response, redirect, url_for, request, session, abort

app = Flask(__name__)
# 设置程序秘钥
app.secret_key = os.getenv('SECRET_KEY', 'secret_key')


@app.route('/')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'xiAoHuaHua')
        res = f'<h1>hello, {name}!</h1>'
    if 'logged_in' in session:
        res += '[Authenticated]-用户已认证'
    else:
        res += '[Not Authenticated]-用户未认证'
    return res


# 后台管理页面视图函数
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403, description='用户未登录!')
    return 'welcome to admin page!'


# 登录视图函数
@app.route('/login')
def login():
    session['logged_in'] = True  # 写入session
    return redirect(url_for('hello'))


# 登出视图函数
@app.route('/logout')
def logout():
    session.pop('logged_in')
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)

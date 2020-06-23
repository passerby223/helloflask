# notes
## 启动开发服务器
* `flask run`命令
    * 从运行命令的当前目录寻找`app.py`和`wsgi.py`模块，并从中寻找名为`app`或`application`的程序实例
    * 从环境变量`FLASK_APP`对应的模块名/导入路径寻找名为`app`或`application`的程序实例
* 使服务器外部可见
    ```bash
    # 会监听所有外部请求，也可以通过环境变量来设置host(详情见`flask run --help`)
    flask run --host=0.0.0.0
    ```
* 改变默认端口
    ```bash
    # 服务器会监听来自端口12306的请求，也可以通过环境变量来设置port(详情见`flask run --help`)
    flask run --port=12306
    ```
## 设置环境变量`FLASK_APP`
* 可以使用Linux系统的`export`命令
    ```bash
    export FLASK_APP=hello
    ```
* 如果使用了`python-dotenv`,那么在使用`flask run`命令或其他命令时会自动从`.flaskenv`和`.env`文件中加载环境变量。
    * 安装`python-dotenv`
        ```bash
        pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple python-dotenv
        ```
    * 当安装了`python-dotenv`时，flask加载环境变量的优先级为`手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量`
    * 可以在同时开发多个Flask程序时，使用`.flaskenv`文件中设置的`FLASK_APP`环境变量来对`app`进行灵活切换
## 模板与静态文件
flask中`模板文件`默认存放在`项目根目录`中的`templates`文件夹中，`静态文件`默认存放在`static`文件夹中，**这两个文件夹需要和包含是程序实例的模块处于同一个目录下**，对应的`项目结构示例`如下所示
```bash
hello/
    - app.py
    - static/
    - templates/
```
## CDN概念
* CDN指分布式服务器系统。
* 服务商把你需要的资源存储在分布于不同地理位置的多个服务器，它会根据用户的地理位置来就近分配服务器提供服务(服务器越近，资源传送就越快)。
* 使用CDN服务可以加快网页资源的加载速度，从而优化用户体验。
* 对于开源的CSS和JavaScript库，CDN提供商通常会免费提供服务。

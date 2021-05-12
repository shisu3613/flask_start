from flask import Flask
app = Flask(__name__) # 首先我们从flask 包里面 导入 Flask 类，通过实例化这个类，创建一个对象 app

#接下来我们需要注册一个处理函数，这个处理函数是处理某个请求的函数，flask官方把他叫做视图函数，即此处的hello
#所谓注册，就是给这一函数加上一个装饰器的帽子，我们使用route 将函数绑定在固定的url上,当用户访问这个地址的时候
#就会触发这个函数，获取，并且把返回值显示在浏览器窗口上
#此处是相对地址， 即是http://127.0.0.1:5000/

#因此整个请求如下：
#1.用户访问http://127.0.0.1:5000/
#2，服务器解析请求，检索到对应的处理函数
#3.获取 hello() 函数的返回值(这里值得注意的是返回值作为响应的主体，会被浏览器默认用HTML格式解析，所以我们可以添加一个html元素标记)
#4.浏览器接受响应将其显示在窗口上

#注意这里加载图片花了很长时间，原因是自身网站用宝塔搭建，然后启用了防盗链设置，没法在外站加载图片，在本地连接调试时需要注释防盗链的配置代码
# @app.route('/')
# def hello():
#     #return 'hello world'
#     #return '<h1>hello world</h1><img src="http://yudingwang.top/海豹.jpeg">'
#     return '<h1>Hello Totoro!</h1><img src="https://yudingwang.top/totoro.gif">'

#修改app.route里面的规则（传入route里面的函数之所以被称作规则是为这里面的也可以定义URL变量
#@app.route('/')（错误）
# @app.route('/<name>')
# def img(name):
#     return '<h1>Hello Totoro!</h1><img src="https://yudingwang.top/totoro.gif">'
#这样不管你访问的是什么‘/1’‘/2’，都会弹出图片
#这里注意因为有了传入的参数，所以route里面的url如果为空会报错

#修改视图函数
#视图函数名称同样可以被调用
from flask import url_for
@app.route('/')
def hello():
    return 'hello world'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))#调用视图函数 hello
    print(url_for('user_page',name='yuding'))#输出 user/yuding
    print(url_for('test_url_for'))# 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL后面。
    print(url_for('test_url_for',num=2)) #输出  /test?num=2

    return 'test_page'

from flask import Flask

app=Flask(__name__)
@app.route('/')#装饰器
#route 装饰器来告诉 Flask 触发函数的 URL 


def index():

    return 'hello world'

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(
    __name__,  # 将这个参数作为程序名称。当然这个是可以自定义的
    static_folder="static",  # 定义静态资源文件夹，默认为 static
    static_url_path="/static",  # 静态资源访问地址，默认为 /static
    template_folder="templates",  # 模板文件夹，默认为 template
)


@app.route("/")  # 请求这个路径，就会执行下面这个函数
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",  # IP
        port=8080,  # 端口
        debug=True,  # 开启调试模式
    )





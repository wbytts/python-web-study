# 需要安装 pip install python-dotenv 时flask才会读取（.env 和 .flaskenv）
# 读取顺序：命令行指定 > .env > .flaskenv
# 注：.env文件如果写注释的话，pipenv貌似会报错，编码问题？
FLASK_APP = 'app'
FLASK_ENV = 'development'
FLASK_RUN_HOST = '0.0.0.0'
FLASK_RUN_PORT = '5000'
FLASK_DEBGU = 1



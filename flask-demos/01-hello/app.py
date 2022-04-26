from flask import Flask, jsonify, request
from flask.templating import render_template
import configs
from exts import load_sqlalchemy, db
from routes import user_bp, test_bp
from werkzeug.routing import BaseConverter

# 初始化app实例
app = Flask(__name__, static_folder='static', template_folder='templates')
# 加载配置文件
app.config.from_object(configs)
# 加载 sqlalchemy
load_sqlalchemy(app)


# 首页，显示路由规则
@app.route("/")
def index():
    rules = list(app.url_map.iter_rules())
    return render_template('url-map-rules.html', rules=rules)


# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(test_bp, url_prefix='/test')


# flask命令：初始化数据库
@app.cli.command('db-init')
def cmd_db_create_all():
    db.create_all()


# 通过 app.add_url_rule 添加路由规则
# app.add_url_rule('/test/add_url_rule', view_func=index)


'''
自定义路由变量转换器：
    导入 BaseConverter：from werkzeug.routing import BaseConverter
    新建类继承 BaseConverter
'''

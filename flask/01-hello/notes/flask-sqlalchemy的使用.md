
安装：`pip install flask-sqlalchemy`

安装：`pip install pymysql`

```py
from flask_sqlalchemy import SQLAlchemy

# 创建数据库操作的 SQLAlchemy对象
db = SQLAlchemy()

# db绑定app
db.init_app(app)


# 创建模型
from exts import db

# 用户表 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
```




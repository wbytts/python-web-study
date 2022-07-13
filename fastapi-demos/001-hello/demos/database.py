from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm.session import sessionmaker  # type: ignore

SQLALCHEMY_DATABASE_URL = 'sqlite:///../db.sqlite3'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encodings='utf8',
    echo=True,
    connect_args={'check_same_thread': False}  # 配置SQLite数据库的时候要使用
)

# 在SQLAlchemy中，SQL是通过会话进行的，我们必须先创建会话
# sessionmaker会产生一个Session类，这个类的实例就是一个数据库的 session
# flush是指发送数据库语句到数据库，但数据库不一定执行写入磁盘
# commit指提交事务，将变更保存到数据库文件
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

# 创建基本映射类
Base = declarative_base(bind=engine, name='Base')

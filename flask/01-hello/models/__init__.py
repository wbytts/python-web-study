from exts import db
import json


def model_to_json(m, cls):
    '''获取表里面的列并存到字典里面'''
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(m, c.name)
        d[c.name] = v
    return d


# 用户表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __str__(self):
        return f'[{self.id}, {self.username}, {self.email}]'

    def to_json(self):
        return model_to_json(self, self.__class__)

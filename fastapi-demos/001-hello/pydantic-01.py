from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = "xxx"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2022-12-22 12:22",
    "friends": [1, 2, "3"],  # "3" 是可以 int("3") 的
}


def red_line(text):
    print(f"\033[31m{text}\033[0m")


user = User(**external_data)
red_line("----------")
print(user.id, user.friends)
print(repr(user.signup_ts))
red_line("----------")
print(user.dict())
print(user.json())
print(user.copy())  # 浅拷贝
red_line("----------")
# print(User.parse_obj(obj=external_data))
# print(User.parse_raw(""))
# print(User.parse_file(path=""))
red_line("----------")
print(user.schema())
print(user.schema_json())
print(user.construct())  # 不校验数据，直接创建模型类
red_line("----------")

# 定义模型类的时候，所有字段都注明类型，字段顺序就不会乱
print(User.__fields__.keys())

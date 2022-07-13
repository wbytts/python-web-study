from fastapi import FastAPI, Path, Cookie
from typing import Optional
from pydantic import BaseModel
from enum import Enum


app = FastAPI()


class Hobby(str, Enum):
    lanqiu = '篮球'
    zuqiu = '足球'


class User(BaseModel):
    username: str
    password: str
    hobby: Optional[Hobby] = Hobby.lanqiu


@app.get("/hello/{name}", summary="打招呼")
def hello(hob: Hobby):
    """
    这是一个会返回你好的接口
    """
    return "你好" + hob

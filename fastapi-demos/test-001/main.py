from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List, Set, Dict, Tuple
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(title="后端")


class User(BaseModel):
    name: str
    sex: str
    age: int


@app.get(
    "/",
    summary="接口名称",
    description="接口的描述",
    tags=["test"],
    response_description="响应的描述",
    deprecated=False,  # 是否过时
    name="namenamename",
)
def root(a: int, b: int):
    """
    这是一个接口
    这里也可以使用 description="xxxxx" 来指定（会被description覆盖）
    """
    return {"message": "Hello World"}


@app.post("/user/queryAll", summary="查询所有用户", tags=["user"])
def query_all_user():
    return {"message": "success"}


@app.post("/user/queryPage", summary="分页查询用户", tags=["user"])
def query_user_page(user: User):
    return {"message": "success"}







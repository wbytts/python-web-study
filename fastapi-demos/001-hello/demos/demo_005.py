from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Optional

router = APIRouter()


@router.get('/hello')
def hello():
    return 'Hello World'


"""
创建一个依赖   
依赖不区分同步函数还是异步函数，可以互相使用
"""


def common_parameters(
    queryString: Optional[str] = '',
    pageNum: int = 1,
    pageSize: int = 10,
):
    return {"queryString": queryString, "pageNum": pageNum, "pageSize": pageSize}


@router.get('/dependency01')
def dependency01(
    commons: dict = Depends(common_parameters)
):
    return commons


# 类作为依赖
class CommonQueryParams:
    def __init__(self, queryString: Optional[str] = None, pageNum: int = 1, pageSize: int = 10):
        self.queryString = queryString
        self.pageNum = pageNum
        self.pageSize = pageSize


@router.get('/dependency02')
def dependency02(
    commons=Depends(CommonQueryParams)
):
    response = {}
    if commons.queryString:
        response.update({"queryString": commons.queryString})
    return response


"""
子依赖的创建和调用
"""


def dep1(q: Optional[str] = None):
    return q


def dep2(q: str = Depends(dep1), x: int = 2):
    if not q:
        return x
    return q


@router.get('/sub_dependency')
def sub_dependency(x=Depends(dep2)):
    return x



"""在路径操作中导入依赖"""
def verify_key(x_key: str = Header(...)):
    """没有返回值的子依赖"""
    if x_key != '123456':
        raise HTTPException(status_code=400, detail='key无效')
    return x_key

def verify_token(x_token: str = Header(...)):
    """没有返回值的子依赖"""
    if x_token != '123456':
        raise HTTPException(status_code=400, detail='token无效')
    return x_token

@router.get(
    '/dependency_in_path_operation',
    dependencies=[Depends(verify_key), Depends(verify_token)]
)
def dependency_in_path_operation():
    return 'yes!!!'



"""
使用 yield 的依赖
需要python3.7才支持
python3.6需要 pip install async-exit-stack async-generator
"""

def get_db():
    db = 'a db'  # 伪代码
    try:
        yield db
    finally:
        "db.close()"


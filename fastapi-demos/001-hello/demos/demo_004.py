from fastapi import APIRouter, status, Form, File, UploadFile, HTTPException
from typing import Optional, List, Union
from pydantic import BaseModel, EmailStr

router = APIRouter()


@router.get('/hello')
def hello():
    return 'Hello World'


"""Response Model 响应模型"""


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    mobile: str = "10086"
    address: str = ""
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    mobile: str = "10086"
    address: str = ""
    full_name: Optional[str] = None


@router.post(
    '/response_model',
    response_model=UserOut,  # 指定返回的结构（可以用列表指定多个）
    # response_class=,
    response_model_exclude_unset=False,  # 不返回默认值
    response_model_include=["username"],  # 返回包含
    response_model_exclude=['password'],  # 返回不包含
    response_description='返回的描述',
    response_model_exclude_none=False,
    # response_model_by_alias='',
    # response_model_exclude_defaults='',
)
def response_model(
    user: UserIn
):
    return user


"""响应状态码 Response Status Code"""


@router.post('/response_status', status_code=status.HTTP_200_OK)
def status_code():
    return {"status_code": status.HTTP_200_OK}


"""
表单数据处理
用Form表单需要 pip install python-multipart
"""


@router.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return username, password


"""Request Files 单文件、多文件上传及参数详解"""


@router.post('/file/upload')
def file_upload(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post('/file/uploadList')
def file_upload_list(files: List[bytes] = File(...)):
    return {"file_count": len(files)}


@router.post('/upload/big')
def upload_big(file: UploadFile = File(...)):
    """
    使用UploadFile类的优势
    1. 文件存储在内存中，使用内存达到一定阈值后，将被保存在磁盘中
    2. 适合图片、视频等大文件
    3. 可以获取上传的文件的元数据，如文件名，创建时间等
    4. 有文件对象的异步接口
    5. 上传的文件对象是python的文件对象，可以直接使用python文件相关的方法
    """
    return {"file_size": len(file)}


"""Path Operation Configuration 路径操作配置"""


@router.post(
    '/path_operation_configuration/',
    response_model=UserOut,
    # tags=["Path", "Operation", "configuration"],
    summary="接口的summary",
    description="接口的描述内容",  # 下面方法的文档字符串也会变成description（会被这个覆盖）
    response_description="响应内容的描述",
    status_code=status.HTTP_200_OK
)
def path_operation_configuration(user: UserIn):
    """
    你好啊
    """
    return user.dict()


@router.post('/dododo')
def do_something(
    name: str = '',  # 要做的事情的名字
):
    return 'yes'


"""错误处理 Handling Errors"""


@router.get('/http_exception')
def http_exception(cityname: str):
    if cityname != 'Beijing':
        raise HTTPException(status_code=404, detail="Not Found", headers={"X-Error": "Error"})


@router.get('/http_exception/{id}')
def http_exception_override(id: str):
    if id != '123':
        raise HTTPException(status_code=418, detail="id 不是 123", headers={"X-Error", "Error"})
    return {"id": id}






import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
import uvicorn  # type: ignore
import demos as router_demos
from starlette.exceptions import HTTPException as StarletteHTTPException

os.system('chcp & cls')

templates = Jinja2Templates(directory='./templates')

app: FastAPI = FastAPI(
    title="标题~~~",
    description="描述~",
    version="1.0.0",
    docs_url="/docs",  # 自定义swagger文档地址
    redoc_url="/redoc",  # 自定义redoc文档地址
    openapi_url="/openapi.json",  # 自定义openapi地址
    openapi_tags=None,
    openapi_prefix='',
    swagger_ui_parameters={},  # swagger ui 配置
    root_path='',
    dependencies=[],  # 这里定义的是全局依赖
)

# mount 表示将某个目录下一个完全独立的应用挂在过来（这个不会在文档中显示）
# 挂载静态文件
app.mount(path='/static', app=StaticFiles(directory='./static'), name='static')


# 重写HTTPException的异常处理
@app.exception_handler(StarletteHTTPException)
def handler_http_exception(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
def handler_request_validation_error(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


app.include_router(router_demos.demo_001, prefix="/demo-001", tags=['001: Hello World'])
app.include_router(router_demos.demo_002, prefix="/demo-002", tags=['002: 路径参数'])
app.include_router(router_demos.demo_003, prefix="/demo-003", tags=['003: 请求参数和验证'])
app.include_router(router_demos.demo_004, prefix="/demo-004", tags=['004: 响应处理和FastAPI配置'])
app.include_router(router_demos.demo_005, prefix="/demo-005", tags=['005: FastAPI的依赖注入系统'])
app.include_router(router_demos.demo_006, prefix="/demo-006", tags=['006: 安全、认证、授权'])

if __name__ == '__main__':
    uvicorn.run('run:app', host="0.0.0.0", port=8000, reload=True, debug=True, workers=8)




from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List, Set, Dict, Tuple
from pydantic import BaseModel, Field, HttpUrl
import os

os.system('chcp & cls')

"""
fastapi的安装：
    完整安装：pip install fastapi[all]
    分开安装：
        pip install fastapi
        pip install uvicorn[standard]
        ......
"""

"""
uvicorn，你可以将其用作运行代码的服务器
创建main.py，创建FastAPI对象app
启动命令：uvicorn main:app --reload
        main：main.py 文件（一个 Python「模块」）。
        app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
        --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
        
    uvicorn main:app --host '0.0.0.0' --port 8080 --reload
"""

"""
默认提供的文档,接口信息等：
    /docs （SwaggerUI提供）
    /redoc （ReDoc提供）
    /openapi.json （OpenAPI在API场景下是一种规定如何定义 API 模式的规范。）
"""

# 导入 FastAPI
# FastAPI 是直接从 Starlette 继承的类。
# 你可以通过 FastAPI 使用所有的 Starlette 的功能。
# from fastapi import FastAPI

# 创建一个 FastAPI「实例」
# 这个实例将是创建你所有 API 的主要交互对象。
app: FastAPI = FastAPI(
    title="整体标题",  # 标题
    description="整体描述",  # 整体描述
)


# 创建一个路径操作
# 这里的「路径」指的是 URL 中从第一个 / 起的后半部分。
@app.get(
    "/",  # 「路径」也通常被称为「端点」或「路由」。
    tags=["test"],
    summary="这是summary",  # 注释
    description="这是description",  # 接口描述
    response_description="响应的描述",  # 响应描述
    status_code="200",  # 状态码
    # deprecated=True, # 标注是否废弃
)
async def root():  # 定义路径操作函数（async是可选的）
    # 返回内容
    # 你可以返回一个 dict、list，像 str、int 一样的单个值，等等。
    # 你还可以返回 Pydantic 模型
    return {"message": "Hello World"}


# 路径参数
@app.get("/items/{item_id}", tags=["items"])  # 路径参数 item_id 的值将作为参数 item_id 传递给你的函数。
# 路径参数在路径操作函数中可以声明类型，这将为你的函数提供编辑器支持，包括错误检查、代码补全等等。
# FastAPI 通过上面的类型声明提供了对请求的自动"解析"。
# 通过同样的 Python 类型声明，FastAPI 提供了数据校验功能。（清楚地指出了校验未通过的具体原因）
async def read_item(item_id: int):
    return {"item_id": item_id}


class ModelName(str, Enum):
    """
    创建一个 Enum 类
    导入 Enum 并创建一个继承自 str 和 Enum 的子类。
    通过从 str 继承，API 文档将能够知道这些值必须为 string 类型并且能够正确地展示出来。
    然后创建具有固定值的类属性，这些固定值将是可用的有效值
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 然后使用你定义的枚举类（ModelName）创建一个带有类型标注的路径参数：
@app.get("/models/{model_name}", tags=["model"])
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


"""
OpenAPI 不支持任何方式去声明路径参数以在其内部包含路径，因为这可能会导致难以测试和定义的情况出现。
不过，你仍然可以通过 Starlette 的一个内部工具在 FastAPI 中实现它。
而且文档依旧可以使用，但是不会添加任何该参数应包含路径的说明。
"""


# 路径转换器
# 你可以使用直接来自 Starlette 的选项来声明一个包含路径的路径参数：
# 在这种情况下，参数的名称为 file_path，结尾部分的 :path 说明该参数应匹配任意的路径。
@app.get("/files/{file_path:path}", tags=["file"])
async def read_file(file_path: str):
    return {"file_path": file_path}


# 查询参数
# 声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数
# 查询字符串是键值对的集合，这些键值对位于 URL 的 ？ 之后，并以 & 符号分隔。
# 由于它们是 URL 的一部分，因此它们的"原始值"是字符串。
# 但是，当你为它们声明了 Python 类型（在上面的示例中为 int）时，它们将转换为该类型并针对该类型进行校验。
# 应用于路径参数的所有相同过程也适用于查询参数
# 由于查询参数不是路径的固定部分，因此它们可以是可选的，并且可以有默认值。


@app.get("/items/", tags=["items"])
async def read_item_1(skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip: skip + limit]


# 可选参数：通过同样的方式，你可以将它们的默认值设置为 None 来声明可选查询参数
@app.get("/items/{item_id}", tags=["items"])
async def read_item_2(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


"""
你可以同时声明多个路径参数和查询参数，FastAPI 能够识别它们。
而且你不需要以任何特定的顺序来声明。
它们将通过名称被检测到
"""

"""
必须查询参数：
    当你为非路径参数声明了默认值时（目前而言，我们所知道的仅有查询参数），则该参数不是必需的。
    如果你不想添加一个特定的值，而只是想使该参数成为可选的，则将默认值设置为 None。
    但当你想让一个查询参数成为必需的，不声明任何默认值就可以
"""

"""
请求体：
    当你需要将数据从客户端（例如浏览器）发送给 API 时，你将其作为「请求体」发送。
    请求体是客户端发送给 API 的数据。响应体是 API 发送给客户端的数据。
    你的 API 几乎总是要发送响应体。但是客户端并不总是需要发送请求体。
    我们使用 Pydantic 模型来声明请求体，并能够获得它们所具有的所有能力和优点。
    注：你不能使用 GET 操作（HTTP 方法）发送请求体，要发送数据，你必须使用下列方法之一：POST（较常见）、PUT、`DELETE` 或 PATCH。
"""


# 首先，你需要从 pydantic 中导入 BaseModel
# from pydantic import BaseModel
# 然后，将你的数据模型声明为继承自 BaseModel 的类，使用标准的 Python 类型来声明所有属性
# 和声明查询参数时一样，当一个模型属性具有默认值时，它不是必需的。否则它是一个必需属性。将默认值设为 None 可使其成为可选属性。


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/", tags=["items"])
# 使用与声明路径和查询参数的相同方式声明请求体，即可将其添加到「路径操作」中
async def create_item(item: Item):
    return item


# 请求体 + 路径参数
# 你可以同时声明路径参数和请求体。
# FastAPI 将识别出与路径参数匹配的函数参数应从路径中获取，而声明为 Pydantic 模型的函数参数应从请求体中获取。
@app.put("/items2/{item_id}", tags=["items"])
async def create_item2(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 请求体 + 路径参数 + 查询参数
# 你还可以同时声明请求体、路径参数和查询参数。
# FastAPI 会识别它们中的每一个，并从正确的位置获取数据。
@app.put("/items3/{item_id}", tags=["items"])
async def create_item3(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})  # type: ignore
    return result


"""
函数参数将依次按如下规则进行识别：
    如果在路径中也声明了该参数，它将被用作路径参数。
    如果参数属于单一类型（比如 int、float、str、bool 等）它将被解释为查询参数。
    如果参数的类型被声明为一个 Pydantic 模型，它将被解释为请求体。
"""

"""
不使用 Pydantic：如果你不想使用 Pydantic 模型，你还可以使用 Body 参数
"""

"""
查询参数和字符串校验:
    FastAPI 允许你为参数声明额外的信息和校验
"""


@app.get("/items2/", tags=["items"])
# 我们打算添加约束条件：即使 q 是可选的，但只要提供了该参数，则该参数值不能超过50个字符的长度。
# 为此，首先从 fastapi 导入 Query：from fastapi import FastAPI, Query
async def read_items2(
    q: Optional[str] = Query(None, max_length=50)
):  # 查询参数 q 的类型为 str，默认值为 None，因此它是可选的
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 使用Query作为默认值
# 由于我们必须用 Query(None) 替换默认值 None，Query 的第一个参数同样也是用于定义默认值。(具有默认值还会使该参数成为可选参数)
@app.get("/items3/", tags=["items"])
async def read_items3(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 不声明默认值，但需要是必需参数
# ... 这种用法：它是一个特殊的单独值，它是 Python 的一部分并且被称为「省略号」
@app.get("/items4/", tags=["items"])
async def read_items4(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 查询参数列表 / 多个值
# 当你使用 Query 显式地定义查询参数时，你还可以声明它去接收一组值，或换句话来说，接收多个值。
# 注：要声明类型为 list 的查询参数，你需要显式地使用 Query，否则该参数将被解释为请求体。
@app.get("/items5/", tags=["items"])
async def read_items5(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# 你也可以直接使用 list 代替 List [str]
# 请记住，在这种情况下 FastAPI 将不会检查列表的内容。
# 例如，List[int] 将检查（并记录到文档）列表的内容必须是整数。但是单独的 list 不会。
@app.get("/items6/", tags=["items"])
async def read_items6(q: list = Query([])):
    query_items = {"q": q}
    return query_items


"""
声明更多元数据
    你可以添加更多有关该参数的信息。
    这些信息将包含在生成的 OpenAPI 模式中，并由文档用户界面和外部工具所使用。
    请记住，不同的工具对 OpenAPI 的支持程度可能不同。
    其中一些可能不会展示所有已声明的额外信息，尽管在大多数情况下，缺少的这部分功能已经计划进行开发。
"""

"""
弃用参数
    现在假设你不再喜欢此参数。
    你不得不将其保留一段时间，因为有些客户端正在使用它，但你希望文档清楚地将其展示为已弃用。
    那么将参数 deprecated=True 传入 Query
"""

"""
路径参数和数值校验:
    与使用 Query 为查询参数声明更多的校验和元数据的方式相同，你也可以使用 Path 为路径参数声明相同类型的校验和元数据。
"""


# 首先，从 fastapi 导入 Path：from fastapi import Path
@app.get("/items7/{item_id}", tags=["items"])
async def read_items7(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 声明元数据
"""
路径参数总是必需的，因为它必须是路径的一部分。
所以，你应该在声明时使用 ... 将其标记为必需参数。
然而，即使你使用 None 声明路径参数或设置一个其他默认值也不会有任何影响，它依然会是必需参数。
"""


@app.get("/items8/{item_id}", tags=["items"])
async def read_items8(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
按需对参数排序
    假设你想要声明一个必需的 str 类型查询参数 q。
    而且你不需要为该参数声明任何其他内容，所以实际上你并不需要使用 Query。
    但是你仍然需要使用 Path 来声明路径参数 item_id。
    如果你将带有「默认值」的参数放在没有「默认值」的参数之前，Python 将会报错。
    但是你可以对其重新排序，并将不带默认值的值（查询参数 q）放到最前面。
    对 FastAPI 来说这无关紧要。它将通过参数的名称、类型和默认值声明（Query、Path 等）来检测参数，而不在乎参数的顺序。

如果你想不使用 Query 声明没有默认值的查询参数 q，同时使用 Path 声明路径参数 item_id，并使它们的顺序与上面不同，Python 对此有一些特殊的语法。
传递 * 作为函数的第一个参数。
Python 不会对该 * 做任何事情，但是它将知道之后的所有参数都应作为关键字参数（键值对），也被称为 kwargs，来调用。即使它们没有默认值。
"""


@app.get("/items9/{item_id}", tags=["items"])
async def read_items9(
    *,
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
数值校验：大于和小于等于
同样的规则适用于：
    gt：大于（greater than）
    le：小于等于（less than or equal）
"""


@app.get("/items10/{item_id}", tags=["items"])
async def read_items10(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
数值校验：浮点数、大于和小于
数值校验同样适用于 float 值。
能够声明 gt 而不仅仅是 ge 在这个前提下变得重要起来。例如，你可以要求一个值必须大于 0，即使它小于 1。
因此，0.5 将是有效值。但是 0.0或 0 不是。
对于 lt 也是一样的。
"""


@app.get("/items11/{item_id}", tags=["items"])
async def read_items11(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
数值校验：
    gt：大于（greater than）
    ge：大于等于（greater than or equal）
    lt：小于（less than）
    le：小于等于（less than or equal）

Query、Path 以及你后面会看到的其他类继承自一个共同的 Param 类（不需要直接使用它）。
而且它们都共享相同的所有你已看到并用于添加额外校验和元数据的参数。
当你从 fastapi 导入 Query、Path 和其他同类对象时，它们实际上是函数。

当被调用时，它们返回同名类的实例。
如此，你导入 Query 这个函数。当你调用它时，它将返回一个同样命名为 Query 的类的实例。
因为使用了这些函数（而不是直接使用类），所以你的编辑器不会标记有关其类型的错误。
这样，你可以使用常规的编辑器和编码工具，而不必添加自定义配置来忽略这些错误。
"""


@app.get("/user/query_all", tags=["user"])
async def user_query_all():
    return {
        "users": [
            {"id": 1, "username": "张三", "age": 18},
            {"id": 2, "username": "李四", "age": 19},
            {"id": 3, "username": "王五", "age": 20},
            {"id": 4, "username": "赵六", "age": 21},
            {"id": 5, "username": "田七", "age": 22},
        ]
    }


@app.get("/zczy/gyl/test-001", tags=["zczy-供应链"])
async def zczy_gyl_test_001():
    return {"msg": "你好啊"}

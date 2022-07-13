from datetime import date

from fastapi import APIRouter, Path, Query, Cookie, Header
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

router = APIRouter()


"""
参数类型：
    路径参数
    查询参数
    请求体
    请求头
    Cookie
"""


class CityInfo(BaseModel):
    name: str = Field(..., example='北京')  # 这个example只是起说明作用，其值不会被验证
    country: str
    country_code: str = None
    country_population: int = Field(default=800, title='人口数量', description='国家的人口数量，这个值必须大于等于800')

    class Config:
        schema_extra = {
            "example": {
                "name": "Shanghai",
                "country": "China",
                "country_code": "CN",
                "country_population": 1400000000,
            }
        }


class CityName(str, Enum):
    Beijing = "北京"
    Shanghai = "上海"


class Data(BaseModel):
    """格式嵌套的请求体"""
    city: List[CityInfo] = None
    date: date
    confirmed: int = Field(ge=0, description="确诊数", default=0)
    deaths: int = Field(ge=0, description="死亡数", default=0)
    recovered: int = Field(ge=0, description="痊愈数", default=0)



@router.get('/query/validations')
def query_params_validate(
    value: str = Query(..., min_length=8, max_length=16, regex="^a"),
    values: List[str] = Query(default=['v1', 'v2'], alias="alias_name")
):
    return value, values


@router.post('/request_body/city')
def get_city_info(city: CityInfo):
    return city


@router.post('/post/city/{name}')
def mix_city_info(
    name: str,
    city01: CityInfo,
    city02: CityInfo,
    confirmed: int = Query(ge=0, description="确诊数", default=0),
    death: int = Query(ge=0, description="死亡数", default=0)
):
    """
    """
    return name, city01.dict(), city02.dict(), confirmed, death


@router.post('/test/data')
def test_data(data: Data):
    return data.dict()


"""如何设置Cookie和Header"""
@router.post('/test/cookie')
def test_cookie(
    cookie_id: Optional[str] = Cookie(None)  # 加上Cookie，会被当做Cookie参数
):
    return cookie_id


@router.post('/test/header')
def test_header(
    header_x: Optional[str] = Header(None, convert_underscores=True)  # convert_underscores表示是否转换下划线
):
    return header_x
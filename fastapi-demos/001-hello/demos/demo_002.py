from datetime import date

from fastapi import APIRouter, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

router = APIRouter()


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


@router.get('/city/{city}')
def city_info(city: str, query_string: Optional[str] = None):
    return {"city": city, "query_string": query_string}


@router.put('/city/{city}')
def result(city: str, city_info: CityInfo):
    return {"city": city, "city_info": city_info}


"""
枚举类型的参数：
    定义一个类，继承 Enum
"""


@router.get('/enum/{city}')
def enum_city(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": '上海', "num": 666}
    elif city == CityName.Beijing:
        return {"city_name": "背景", "num": 999}
    return {"msg": "没有啦~"}


@router.get("/num/{num}")
def get_num(
    # num: int = Path(None, ge=1, le=10, title="一个数字", description="不可描述")
    num: int = Path(..., ge=1, le=10, title="一个数字", description="不可描述")
):
    return {"result": num}


@router.get("/bool/{x}")
def get_bool(
    x: bool = False
):
    """
    值为True：true, True, 非零, on, yes <br />
    值为False：false, False, 0, off, no
    """
    return x


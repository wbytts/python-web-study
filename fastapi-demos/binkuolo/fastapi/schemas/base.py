# -*- coding:utf-8 -*-
"""
@Des: 基础schemas
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union


class BaseResp(BaseModel):
    code: int = Field(description="状态码")
    message: str = Field(description="信息")
    data: Union[List, Dict, BaseModel] = Field(description="数据")


class ResAntTable(BaseModel):
    success: bool = Field(description="状态码")
    data: List = Field(description="数据")
    total: int = Field(description="总条数")


class WebsocketMessage(BaseModel):
    action: Optional[str]
    user: Optional[int]
    data: Optional[Any]


class WechatOAuthData(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str
    unionid: Optional[str]
    scope: str
    openid: str


class WechatUserInfo(BaseModel):
    openid: str
    nickname: str
    sex: int
    city: str
    province: str
    country: str
    headimgurl: str
    unionid: Optional[str]
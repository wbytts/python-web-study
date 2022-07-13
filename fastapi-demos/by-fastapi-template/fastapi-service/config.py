# encoding: utf-8
"""
@author: wbytts
@desc: 
"""
import os
from typing import List
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv  # python-dotenv


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "by-fastapi-service"
    DESCRIPTION: str = '666'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(os.getcwd(), "templates")
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60  # 日


settings = Config()


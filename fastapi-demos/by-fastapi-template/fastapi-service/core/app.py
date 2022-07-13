# encoding: utf-8
"""
@author: wbytts
@desc: 
"""
from fastapi import FastAPI
from config import settings

app = FastAPI(
    debug=settings.APP_DEBUG
)

# encoding: utf-8
"""
@author: wbytts
@desc: 主启动脚本
"""
import os
import uvicorn

if __name__ == '__main__':
    # 解决windows平台控制台乱码的问题
    os.system('chcp & cls')
    # 运行应用
    uvicorn.run(
        app='core:app',
        host="0.0.0.0",
        port=8888,
        reload=True,
        debug=True,
        workers=4
    )






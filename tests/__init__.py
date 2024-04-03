# -*- coding: utf-8 -*-
"""
@File    : __init__.py.py
@Date    : 2023-07-17
"""
import logging

logger = logging.getLogger('stock-open-api')
logger.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter(
    fmt='%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s:\n%(message)s\n',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 输出到控制台
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)

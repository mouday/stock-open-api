# -*- coding: utf-8 -*-
"""
@File    : log_util.py
@Date    : 2023-07-18
"""

import logging

from stock_open_api import config

logger = logging.getLogger('stock-open-api')

# development
if config.STOCK_OPEN_API_DEBUG:
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

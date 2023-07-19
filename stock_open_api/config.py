# -*- coding: utf-8 -*-
"""
@File    : config.py
@Date    : 2023-07-19
"""

try:
    # development
    from environs import Env
except ImportError:
    # production
    class Env(object):
        def read_env(self):
            pass

env = Env()
env.read_env()

STOCK_OPEN_API_DEBUG = env.bool('STOCK_OPEN_API_DEBUG', False)

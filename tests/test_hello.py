# -*- coding: utf-8 -*-
"""
@File    : test_hello.py
@Date    : 2024-01-21
@Author  : Peng Shiyu
"""
import unittest
from stock_open_api.version import VERSION


class HelloTest(unittest.TestCase):
    def test_hi(self):
        print('VERSION:', VERSION)
        assert 'hi' == 'hi'

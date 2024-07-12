# -*- coding: utf-8 -*-
"""
@File    : test_company.py
@Date    : 2023-07-25
"""
import unittest

from stock_open_api.api.xueqiu import xueqiu_market
from stock_open_api.utils import json_util

class MarketTest(unittest.TestCase):
    def test_get_stock_market(self):
        json_util.dump_json(xueqiu_market.get_stock_market('SH600733', english_key=True))

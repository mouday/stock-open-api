# -*- coding: utf-8 -*-
"""
@File    : neeq_stock_test.py
@Date    : 2024-04-02
"""
import unittest

from stock_open_api.api.ipo3 import neeq_stock
from stock_open_api.utils import json_util


class NeeqStockTest(unittest.TestCase):
    def test_get_company_info(self):
        res = neeq_stock.get_company_info('430510')
        json_util.dump_json(res)

    def test_convert_company_info_to_english_key(self):
        res = neeq_stock.get_company_info('430510', english_key=True)
        json_util.dump_json(res)

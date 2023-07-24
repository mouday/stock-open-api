# -*- coding: utf-8 -*-
"""
@File    : test_iterator_util.py
@Date    : 2023-07-24
"""
from stock_open_api.api.eastmoney import us_chinese_stock
from stock_open_api.utils import iterator_util


def test_list_iterator():
    for data in iterator_util.list_iterator(us_chinese_stock.get_list):
        print(data.to_dict())

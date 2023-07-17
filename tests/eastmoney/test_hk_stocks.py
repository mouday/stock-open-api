# -*- coding: utf-8 -*-
"""
@File    : test_hk_stocks.py
@Date    : 2023-07-17
"""
import pytest

from stock_open_api.api.eastmoney import hk_stock


def test_get_list():
    data = hk_stock.get_list()
    print(data.items)


if __name__ == '__main__':
    # Shortcut for --capture=no
    pytest.main(["-s", "test_hk_stocks.py"])

# -*- coding: utf-8 -*-
"""
@File    : xueqiu_util.py
@Date    : 2024-07-12
"""
import re


def parse_stock_code(stock_code):
    """
    北汽蓝谷(SH:600733)
    :return:
    {
     'stock_name': '北汽蓝谷',
     'listing_name': 'SH',
     'stock_code': '600733'
    }
    """
    ret = re.match("(?P<stock_name>.*?)\((?P<listing_name>.*?)\:(?P<stock_code>.*?)\)", stock_code)

    data = {}

    if ret:
        data = {
            'stock_name': ret.groupdict().get('stock_name'),
            'listing_name': ret.groupdict().get('listing_name'),
            'stock_code': ret.groupdict().get('stock_code'),
        }

    return data


if __name__ == '__main__':
    print(parse_stock_code('北汽蓝谷(SH:600733)'))

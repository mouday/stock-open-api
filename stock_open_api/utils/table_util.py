# -*- coding: utf-8 -*-
"""
table_util.py
"""
from parsel import Selector


def parse_table(sel: Selector):
    """
    标准表格解析工具
    :param sel:
    :return:
    """
    lst = []

    # 解析表头
    headers = [x.xpath('string(.)').extract_first('') for x in sel.css('thead th')]

    # 解析内容
    for row in sel.css('tbody tr'):
        item = {}

        for key, value in zip(headers, row.css("td")):
            item[key] = value.xpath('string(.)').extract_first('').strip()

        lst.append(item)

    return lst

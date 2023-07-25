# -*- coding: utf-8 -*-
"""
@File    : test_company.py
@Date    : 2023-07-25
"""
from stock_open_api.api.jqka import company
from stock_open_api.utils import json_util


def test_get_company_info():
    json_util.dump_json(company.get_company_info('300763'))

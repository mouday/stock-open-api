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
        res = neeq_stock.get_company_info('870783')
        json_util.dump_json(res)

    def test_convert_company_info_to_english_key(self):
        res = neeq_stock.get_company_info('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_finance_profit_list(self):
        res = neeq_stock.get_income_statement_list('430510')
        json_util.dump_json(res)

    def test_get_finance_profit_list_to_english_key(self):
        res = neeq_stock.get_income_statement_list('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_balance_sheet_list(self):
        res = neeq_stock.get_balance_sheet_list('430510')
        json_util.dump_json(res)

    def test_get_cash_flow_statement_list(self):
        res = neeq_stock.get_cash_flows_statement_list('430510')
        json_util.dump_json(res)

    def test_get_financial_analysis_list(self):
        res = neeq_stock.get_financial_analysis_list('430510')
        json_util.dump_json(res)




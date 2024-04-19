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

    def test_get_balance_sheet_list_to_english_key(self):
        res = neeq_stock.get_balance_sheet_list('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_cash_flow_statement_list(self):
        res = neeq_stock.get_cash_flow_statement_list('430510')
        json_util.dump_json(res)

    def test_get_cash_flow_statement_list_to_english_key(self):
        res = neeq_stock.get_cash_flow_statement_list('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_financial_analysis_list(self):
        res = neeq_stock.get_financial_analysis_list('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_financial_analysis_list_to_english_key(self):
        res = neeq_stock.get_financial_analysis_list('430510', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_fund_list(self):
        res = neeq_stock.get_stock_fund_list('830936')
        json_util.dump_json(res)

    def test_get_stock_fund_list_to_english_key(self):
        res = neeq_stock.get_stock_fund_list('830936', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_trade_list(self):
        res = neeq_stock.get_stock_trade_list('830936')
        json_util.dump_json(res)

    def test_get_stock_trade_list_to_english_key(self):
        res = neeq_stock.get_stock_trade_list('830936', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_event_list_to_english_key(self):
        res = neeq_stock.get_stock_event_list('830936', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_event_list(self):
        res = neeq_stock.get_stock_event_list('830936')
        json_util.dump_json(res)

    def test_get_stock_notice_list(self):
        res = neeq_stock.get_stock_notice_list('830936')
        json_util.dump_json(res.to_dict())

    def test_get_stock_survey(self):
        res = neeq_stock.get_stock_survey('830936')
        json_util.dump_json(res)

    def test_get_stock_survey_to_english_key(self):
        res = neeq_stock.get_stock_survey('830936', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_funded(self):
        res = neeq_stock.get_stock_funded_list('430283')
        json_util.dump_json(res)

    def test_get_stock_funded_to_english_key(self):
        res = neeq_stock.get_stock_funded_list('430283', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_broker(self):
        res = neeq_stock.get_stock_broker_list('832586')
        json_util.dump_json(res)

    def test_get_stock_broker_to_english_key(self):
        res = neeq_stock.get_stock_broker_list('832586', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_pledge(self):
        res = neeq_stock.get_stock_pledge_data('839826')
        json_util.dump_json(res)

    def test_get_stock_pledge_to_english_key(self):
        res = neeq_stock.get_stock_pledge_data('839826', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_pledge_loan_records(self):
        res = neeq_stock.get_stock_pledge_loan_records('839826')
        json_util.dump_json(res)

    def test_get_stock_pledge_loan_records_to_english_key(self):
        res = neeq_stock.get_stock_pledge_loan_records('839826', english_key=True)
        json_util.dump_json(res)

    def test_get_stock_report_list(self):
        res = neeq_stock.get_stock_report_list('839826')
        json_util.dump_json(res)

    def test_get_stock_report_list_to_english_key(self):
        res = neeq_stock.get_stock_report_list('839826', english_key=True)
        json_util.dump_json(res)

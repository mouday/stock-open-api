# -*- coding: utf-8 -*-
"""
@File    : stock.py
@Date    : 2023-07-25
"""
import warnings

import six

from stock_open_api.items.list_item import ListItem
from stock_open_api.utils import request_util, excel_util, json_util


class StockType(object):
    Stock_A = 'A股列表'
    Stock_B = 'B股列表'
    Stock_CDR = 'CDR列表'
    Stock_AB = 'A＋B股列表'


INDICATOR_MAP = {
    StockType.Stock_A: "tab1",
    StockType.Stock_B: "tab2",
    StockType.Stock_CDR: "tab3",
    StockType.Stock_AB: "tab4",
}


def get_stock_list(stock_type=StockType.Stock_A):
    """
    深圳证券交易所-股票列表
    http://www.szse.cn/market/product/stock/list/index.html

    代码参考：https://github.com/akfamily/akshare/blob/main/akshare/stock/stock_info.py

    :param stock_type: choice of {"A股列表", "B股列表", "CDR列表", "A+B股列表"}
    :type stock_type: str

    :return: 指定 indicator 的数据
    :rtype: ListItem

    >>> get_stock_list
    {
        "total": 2804,
        "list": [
            {
              "板块": "主板",
              "公司全称": "平安银行股份有限公司",
              "英文名称": "Ping An Bank Co., Ltd.",
              "注册地址": "广东省深圳市罗湖区深南东路5047号",
              "A股代码": "000001",
              "A股简称": "平安银行",
              "A股上市日期": "1991-04-03",
              "A股总股本": "19,405,918,198",
              "A股流通股本": "19,405,546,950",
              "B股代码": "",
              "B股简称": "",
              "B股上市日期": "",
              "B股总股本": "0",
              "B股流通股本": "0",
              "地区": "华南",
              "省份": "广东",
              "城市": "深圳市",
              "所属行业": "J 金融业",
              "公司网址": "bank.pingan.com",
              "未盈利": "-",
              "具有表决权差异安排": "-",
              "具有协议控制架构": "-"
            }
        ]
    }
    """
    url = "http://www.szse.cn/api/report/ShowReport"

    params = {
        "SHOWTYPE": "xlsx",
        "CATALOGID": "1110",
        "TABKEY": INDICATOR_MAP[stock_type],
        "random": "0.6935816432433362",
    }

    r = request_util.get(url, params=params)

    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        lst = excel_util.read_excel(six.BytesIO(r.content))

    list_item = ListItem()
    list_item.items = lst
    list_item.total = len(lst)

    return list_item


if __name__ == '__main__':
    json_util.dump_json(get_stock_list().to_dict())

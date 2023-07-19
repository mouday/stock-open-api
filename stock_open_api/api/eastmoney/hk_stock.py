# -*- coding: utf-8 -*-
"""
@File    : hk_stock.py
@Date    : 2023-07-17

港股相关接口
"""

import json

from stock_open_api.api.eastmoney import hk_stock_config
from stock_open_api.items.list_item import ListItem
from stock_open_api.utils import time_util, request_util


def get_list(page=1, size=20):
    """
    港股行情列表

    东方财富网 > 行情中心 > 港股市场 > 全部港股
    http://quote.eastmoney.com/center/gridlist.html#hk_stocks

    :param page: 分页
    :type page: int
    :param size: 分页大小
    :type size: int

    :return: 港股行情列表
    :rtype: ListItem

    >>> get_list()
    {
      "total": 4587,
      "items": [
        {
          "代码": "00491",
          "名称": "英皇文化产业",
          "最新价": 0.075,
          "涨跌额": 0.018,
          "涨跌幅": 31.58,
          "今开": 0.06,
          "最高": 0.078,
          "最低": 0.06,
          "昨收": 0.057,
          "成交量(股)": 28240000,
          "成交额": 2008120.0
        }
      ]
    }
    """
    url = 'http://83.push2.eastmoney.com/api/qt/clist/get'

    params = {
        # 'cb': 'jQuery112408884331980698759_1689562953826',
        'pn': page,  # page num
        'pz': size,  # page size
        'po': 1,
        'np': 1,
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': 2,
        'invt': 2,
        'wbp2u': '|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:128 t:3,m:128 t:4,m:128 t:1,m:128 t:2',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
        # '_': 1689562954034
        '_': time_util.get_timespan_13()
    }

    res = request_util.get(url, params)

    data = res.json()

    list_item = ListItem()
    if data['data'] is None:
        return list_item

    list_item.total = data['data']['total']

    items = []
    for row in data['data']['diff']:
        item = {}

        for map_item in hk_stock_config.list_key_map:
            item[map_item['title']] = row.get(map_item['key'])

        items.append(item)

    list_item.items = items
    return list_item


def get_org_profile(code):
    """
    港股 公司资料

    数据来源：http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile

    :param code: 股票代码 eg: 00491
    :type code: str

    :return: 公司资料
    :rtype: dict

    >>> get_org_profile('00491')
    {
      "证券代码": "00491.HK",
      "公司名称": "英皇文化产业集团有限公司",
      "英文名称": "Emperor Culture Group Limited",
      "注册地": "Bermuda 百慕大",
      "注册地址": "Clarendon House, 2 Church Street, Hamilton, Bermuda",
      "公司成立日期": "1992-03-27",
      "所属行业": "媒体及娱乐",
      "董事长": "范敏嫦",
      "公司秘书": "廖雪盈",
      "员工人数": 598,
      "办公地址": "香港湾仔轩尼诗道288号英皇集团中心28楼",
      "公司网址": "www.empculture.com",
      "E-MAIL": "enquiry@emperorgroup.com",
      "年结日": "06-30",
      "联系电话": "+852 2835-6688",
      "核数师": "安永会计师事务所",
      "传真": "+852 2835-8188",
      "公司介绍": "英皇文化产业集团有限公司(491.HK)主要从事娱乐、媒体及文化发展业务..."
    }

    """
    url = 'https://datacenter.eastmoney.com/securities/api/data/v1/get'

    params = {
        'reportName': 'RPT_HKF10_INFO_ORGPROFILE',
        'columns': 'SECUCODE,SECURITY_CODE,ORG_NAME,ORG_EN_ABBR,BELONG_INDUSTRY,FOUND_DATE,CHAIRMAN,SECRETARY,ACCOUNT_FIRM,REG_ADDRESS,ADDRESS,YEAR_SETTLE_DAY,EMP_NUM,ORG_TEL,ORG_FAX,ORG_EMAIL,ORG_WEB,ORG_PROFILE,REG_PLACE',
        'quoteColumns': '',
        'filter': '(SECUCODE="{}.HK")'.format(code),
        'pageNumber': '1',
        'pageSize': '200',
        'sortTypes': '',
        'sortColumns': '',
        'source': 'F10',
        'client': 'PC',
        'v': '05607491999280683',
    }

    res = request_util.get(url, params)

    data = res.json()['result']['data'][0]

    item = {}
    for row in hk_stock_config.org_profile_key_map:
        value = data.get(row['key'])
        if isinstance(value, str):
            value = value.strip()

        item[row['title']] = value

    return item


def get_security_info(code):
    """
    港股  证券资料

    数据来源：http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile

    :param code: 股票代码 eg: 00491
    :type code: str

    :return: 证券资料
    :rtype: dict

    >>> get_security_info('00491')
    {
      "证券代码": "00491.HK",
      "证券简称": "英皇文化产业",
      "上市日期": "1992-06-10 00:00:00",
      "证券类型": "非H股",
      "交易所": "香港交易所",
      "板块": "主板",
      "最新交易单位（每手股数）": 20000,
      "ISIN（国际证券识别编码）": "BMG3036H1079",
      "是否沪港通标的": "否",
      "是否深港通标的": "否"
    }
    """
    url = 'https://datacenter.eastmoney.com/securities/api/data/v1/get'

    params = {
        'reportName': 'RPT_HKF10_INFO_SECURITYINFO',
        'columns': 'SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,SECURITY_TYPE,LISTING_DATE,ISIN_CODE,BOARD,TRADE_UNIT,TRADE_MARKET,GANGGUTONGBIAODISHEN,GANGGUTONGBIAODIHU',
        'quoteColumns': '',
        'filter': '(SECUCODE="{}.HK")'.format(code),
        'pageNumber': '1',
        'pageSize': '200',
        'sortTypes': '',
        'sortColumns': '',
        'source': 'F10',
        'client': 'PC',
        'v': '05299608968630529',
    }

    res = request_util.get(url, params)

    data = res.json()['result']['data'][0]

    item = {}
    for row in hk_stock_config.security_info_key_map:
        value = data.get(row['key'])
        if isinstance(value, str):
            value = value.strip()

        item[row['title']] = value

    return item


if __name__ == '__main__':
    print(json.dumps(get_list().to_dict(), indent=2, ensure_ascii=False))

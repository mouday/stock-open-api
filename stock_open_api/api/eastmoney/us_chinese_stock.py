# -*- coding: utf-8 -*-
"""
@File    : us_chinese_stock.py
@Date    : 2023-07-17
中国概念股相关接口
"""
import json

from stock_open_api.api.eastmoney import us_chinese_stock_config
from stock_open_api.items.list_item import ListItem
from stock_open_api.log import logger
from stock_open_api.utils import time_util, request_util, json_util


def get_list(page=1, size=20):
    """
    中国概念股 列表

    东方财富网 > 行情中心 > 美股市场 > 中国概念股
    http://quote.eastmoney.com/center/gridlist.html#us_chinese

    :param page: int
    :param size: int

    :return:
    :rtype: ListItem

    >>> get_list()
    {
      "total": 384,
      "items": [
        {
          "代码": "PWM",
          "名称": "盛德财富",
          "最新价(美元)": 17.0,
          "涨跌额": 5.33,
          "涨跌幅": 45.67,
          "开盘价": 10.5,
          "最高价": 19.5,
          "最低价": 10.5,
          "昨收价": 11.67,
          "总市值(美元)": 153000000,
          "市盈率": 112.95
        }
      ]
    }
    """
    url = 'http://45.push2.eastmoney.com/api/qt/clist/get'

    params = {
        # 'cb': 'jQuery1124004782104701641621_1689648873162',
        'pn': page,
        'pz': size,
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'wbp2u': '|0|0|0|web',
        'fid': 'f3',
        'fs': 'b:MK0201',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
        # '_': '1689648873172',
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

        for map_item in us_chinese_stock_config.list_key_map:
            item[map_item['title']] = row.get(map_item['key'])

        items.append(item)

    list_item.items = items
    return list_item


def get_org_profile(code):
    """
    中国概念股 公司资料

    http://emweb.eastmoney.com/PC_USF10/pages/index.html?code=PWM&type=web&color=w#/gsgk/gszl

    :param code: str eg: PWM

    :return:

    >>> get_org_profile('PWM')
    {
      "证券代码": "PWM.O",
      "公司名称": "Prestige Wealth Inc.",
      "中文名称": "盛德财富有限公司",
      "注册地址": null,
      "成立日期": "2018-10-25",
      "所属行业": "投资银行业与经纪业",
      "主席": "Hongtao Shi(师鸿涛)",
      "员工人数": 6,
      "办公地址": "香港中环皇后大道中2号长江集团中心51楼5102室",
      "公司网址": "www.prestigewealthinc.com",
      "E-MAIL": null,
      "电话号码": "+852 2122-8560",
      "传真号码": "+852 2122 8589",
      "公司介绍": "盛德财富有限公司是一家在开曼群岛注册成立的境外控股母公司,主要由其境内实体子公司Prestige Financial Holdings Group Limited运营。盛德财富有限公司(“PWI”,或“公司”)是一家于2018年10月25日根据开曼群岛法律成立的有限公司。该公司通过其子公司向高净值和超高净值个人和企业提供私人财富管理服务和资产管理。"
    }
    """
    detail_url = 'http://emweb.eastmoney.com/PC_USF10/pages/index.html?code={}&type=web&color=w#/gsgk/gszl'.format(code)
    logger.debug(detail_url)

    url = 'https://datacenter.eastmoney.com/securities/api/data/v1/get'

    params = {
        'reportName': 'RPT_USF10_INFO_ORGPROFILE',
        'columns': 'SECUCODE,SECURITY_CODE,ORG_CODE,SECURITY_INNER_CODE,ORG_NAME,ORG_EN_ABBR,BELONG_INDUSTRY,FOUND_DATE,CHAIRMAN,REG_PLACE,ADDRESS,EMP_NUM,ORG_TEL,ORG_FAX,ORG_EMAIL,ORG_WEB,ORG_PROFILE',
        'quoteColumns': '',
        'filter': '(SECURITY_CODE="{}")'.format(code),
        'pageNumber': '1',
        'pageSize': '200',
        'sortTypes': '',
        'sortColumns': '',
        'source': 'SECURITIES',
        'client': 'PC',
        'v': '016960969044233054',
    }

    res = request_util.get(url, params)

    data = res.json()['result']['data'][0]

    item = {}
    for row in us_chinese_stock_config.org_profile_key_map:
        value = data.get(row['key'])
        if isinstance(value, str):
            value = value.strip()

        item[row['title']] = value

    return item


def get_security_info(code):
    """
    中国概念股 证券资料

    数据源：http://emweb.eastmoney.com/PC_USF10/pages/index.html?code=PWM&type=web&color=w#/gsgk/zqzl

    :param code: str eg: PWM.O

    - 通过 get_org_profile() 的`证券代码` 字段获取
    - eg: "证券代码": "PWM.O"

    :return:

    >>> get_security_info('PWM.O')
    {
      "证券代码": "PWM",
      "上市日期": "2023-07-06",
      "证券类型": "美股",
      "上市场所": "NASDAQ",
      "ISIN": "KYG7244A1013",
      "每股面值": "0.000625 USD",
      "ADS折算比": null,
      "年结日": "09-30"
    }
    """
    logger.debug('http://emweb.eastmoney.com/PC_USF10/pages/index.html?code={}&type=web&color=w#/gsgk/zqzl'.format(code))
    url = 'https://datacenter.eastmoney.com/securities/api/data/v1/get'

    params = {
        'reportName': 'RPT_USF10_INFO_SECURITYINFO',
        'columns': 'SECUCODE,SECURITY_CODE,ORG_CODE,SECURITY_INNER_CODE,SECURITY_TYPE,LISTING_DATE,ISIN_CODE,TRADE_MARKET,YEAR_SETTLE_DAY,PAR_VALUE,CONVERT_RATIO,ISSUE_PRICE,ISSUE_NUM',
        'quoteColumns': '',
        'filter': '(SECUCODE="{}")'.format(code),
        'pageNumber': '1',
        'pageSize': '200',
        'sortTypes': '',
        'sortColumns': '',
        'source': 'SECURITIES',
        'client': 'PC',
        'v': '034528884905654467',
    }

    res = request_util.get(url, params)

    data = res.json()['result']['data'][0]

    logger.debug(json_util.format_json(data))

    item = {}

    for row in us_chinese_stock_config.security_info_key_map:
        value = data.get(row['key'])

        if isinstance(value, str):
            value = value.strip()

        # 上市日期
        if row['key'] == 'LISTING_DATE' and value:
            value = value.split(' ')[0]

        item[row['title']] = value

    return item


if __name__ == '__main__':
    # print(json.dumps(get_list().to_dict(), indent=2, ensure_ascii=False))
    # print(json.dumps(get_org_profile('WXT'), indent=2, ensure_ascii=False))
    print(json.dumps(get_security_info('WXT.O'), indent=2, ensure_ascii=False))

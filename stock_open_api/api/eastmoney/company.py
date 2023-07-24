# -*- coding: utf-8 -*-
"""
@File    : company.py
@Date    : 2023-07-18
"""
import json

from stock_open_api.api.eastmoney import company_config
from stock_open_api.utils import request_util


def get_company_info(code):
    """
    公司 基本资料 | 发行相关

    http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801

    :param code: 股票代码
    :type code: str

    - eg:
    - 深圳证券交易所 SZ301398 或者 sz301398
    - 上海证券交易所 SH688627 或者 sh688627

    :return: 基本资料 + 发行相关
    :rtype: dict

    >>> get_company_info('603801')
    {
      "公司名称": "志邦家居股份有限公司",
      "英文名称": "Zbom Home Collection Co.,Ltd",
      "A股代码": "603801",
      "A股简称": "志邦家居",
      "A股扩位简称": null,
      "曾用名": "志邦股份",
      "B股代码": null,
      "B股简称": null,
      "H股代码": null,
      "H股简称": null,
      "证券类别": "上交所主板A股",
      "上市交易所": "上海证券交易所",
      "所属东财行业": "轻工制造-家具-家具制造",
      "所属证监会行业": "制造业-家具制造业",
      "总经理": "许帮顺",
      "法人代表": "孙志勇",
      "董秘": "孙娟",
      "董事长": "孙志勇",
      "证券事务代表": "臧晶晶",
      "独立董事": "鲁昌华,张京跃,王文兵",
      "联系电话": "0551-67186564",
      "电子信箱": "zbom@zbom.com",
      "传真": "0551-65203999",
      "公司网址": "www.zbom.com",
      "办公地址": "安徽省合肥市庐阳工业区连水路19号",
      "注册地址": "安徽省合肥市庐阳工业区连水路19号",
      "区域": "安徽",
      "邮政编码": "230061",
      "注册资本(元)": 43654.7813,
      "工商登记": "91340100772816763N",
      "雇员人数": 5151,
      "管理人员人数": 16,
      "律师事务所": "安徽天禾律师事务所",
      "会计师事务所": "大华会计师事务所(特殊普通合伙)",
      "公司介绍": "志邦家居股份有限公司创立于1998年,是中国厨柜行业的先行者...",
      "经营范围": "家具制造;家具零配件生产;家具零配件销售...",
      "成立日期": "2005-04-04",
      "上市日期": "2017-06-30",
      "发行市盈率(倍)": 22.92,
      "网上发行日期": "2017-06-20",
      "发行方式": "网上定价发行,网下询价配售,市值申购",
      "每股面值(元)": 1,
      "发行量(股)": 40000000,
      "每股发行价(元)": 23.47,
      "发行费用(元)": 89434000,
      "发行总市值(元)": 938800000,
      "募集资金净额(元)": 849366000,
      "首日开盘价(元)": 33.8,
      "首日收盘价(元)": 33.8,
      "首日换手率": 0.0914,
      "首日最高价(元)": 33.8,
      "网下配售中签率": 0.02743221,
      "定价中签率": 0.03205759
    }

    """
    url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/PageAjax'

    params = {
        'code': code
    }

    res = request_util.get(url, params)

    company_info = res.json()['jbzl'][0]
    security_info = res.json()['fxxg'][0]

    company_info.update(security_info)

    item = {}
    for row in company_config.company_key_map:
        value = company_info.get(row['key'])
        if isinstance(value, str):
            value = value.strip()

        # 上市日期 成立日期 网上发行日期
        # fix: AttributeError: 'NoneType' object has no attribute 'split'
        if row['key'] in ['LISTING_DATE', 'FOUND_DATE', 'ONLINE_ISSUE_DATE'] and value:
            value = value.split(' ')[0]

        item[row['title']] = value

    return item


if __name__ == '__main__':
    print(json.dumps(get_company_info('sh603801'), indent=2, ensure_ascii=False))

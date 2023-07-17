# -*- coding: utf-8 -*-
"""
@File    : hk_stocks_config.py
@Date    : 2023-07-17
"""
from stock_open_api.utils import ua_util

headers = {
    'User-Agent': ua_util.User_Agent
}

# 配置数据
# http://quote.eastmoney.com/center/js/gridlist.js
# 港股--全部

list_key_map = [
    {
        "title": "代码",
        "key": "f12",
        "name": "Code"
    },
    {
        "title": "名称",
        "key": "f14",
        "name": "Name"
    },

    {
        "title": "最新价",
        "key": "f2",
        "name": "Close"
    },
    {
        "title": "涨跌额",
        "key": "f4",
        "name": "Change"
    },
    {
        "title": "涨跌幅",
        "key": "f3",
        "name": "ChangePercent"
    },
    {
        "title": "今开",
        "key": "f17",
        "name": "Open"
    },
    {
        "title": "最高",
        "key": "f15",
        "name": "Hign"
    },
    {
        "title": "最低",
        "key": "f16",
        "name": "Low"
    },
    {
        "title": "昨收",
        "key": "f18",
        "name": "PreviousClose"
    },
    {
        "title": "成交量(股)",
        "key": "f5",
        "name": "Volume"
    },
    {
        "title": "成交额",
        "key": "f6",
        "name": "Amount"
    }
]

# 公司资料
org_profile_key_map = [
    {
        "title": "证券代码",
        "key": "SECUCODE",
    },
    {
        "title": "公司名称",
        "key": "ORG_NAME",
    },
    {
        "title": "英文名称",
        "key": "ORG_EN_ABBR",
    },
    {
        "title": "注册地",
        "key": "REG_PLACE",
    },
    {
        "title": "注册地址",
        "key": "REG_ADDRESS",
    },
    {
        "title": "公司成立日期",
        "key": "FOUND_DATE",
    },
    {
        "title": "所属行业",
        "key": "BELONG_INDUSTRY",
    },
    {
        "title": "董事长",
        "key": "CHAIRMAN",
    },
    {
        "title": "公司秘书",
        "key": "SECRETARY",
    },
    {
        "title": "员工人数",
        "key": "EMP_NUM",
    },
    {
        "title": "办公地址",
        "key": "ADDRESS",
    },
    {
        "title": "公司网址",
        "key": "ORG_WEB",
    },
    {
        "title": "E-MAIL",
        "key": "ORG_EMAIL",
    },
    {
        "title": "年结日",
        "key": "YEAR_SETTLE_DAY",
    },
    {
        "title": "联系电话",
        "key": "ORG_TEL",
    },
    {
        "title": "核数师",
        "key": "ACCOUNT_FIRM",
    },
    {
        "title": "传真",
        "key": "ORG_FAX",
    },
    {
        "title": "公司介绍",
        "key": "ORG_PROFILE",
    },
]

# 证券资料
security_info_key_map = [
    {
        "title": "证券代码",
        "key": "SECUCODE",
    },
    {
        "title": "证券简称",
        "key": "SECURITY_NAME_ABBR",
    },
    {
        "title": "上市日期",
        "key": "LISTING_DATE",
    },
    {
        "title": "证券类型",
        "key": "SECURITY_TYPE",
    },
    {
        "title": "交易所",
        "key": "TRADE_MARKET",
    },
    {
        "title": "板块",
        "key": "BOARD",
    },
    {
        "title": "最新交易单位（每手股数）",
        "key": "TRADE_UNIT",
    },
    {
        "title": "ISIN（国际证券识别编码）",
        "key": "ISIN_CODE",
    },
    {
        "title": "是否沪港通标的",
        "key": "GANGGUTONGBIAODIHU",
    },
    {
        "title": "是否深港通标的",
        "key": "GANGGUTONGBIAODISHEN",
    },
]

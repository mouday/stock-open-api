# -*- coding: utf-8 -*-
"""
@File    : us_chinese_stock_config.py
@Date    : 2023-07-17
中国概念股相关接口
"""

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
        "title": "最新价(美元)",
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
        "title": "开盘价",
        "key": "f17",
        "name": "Open"
    },
    {
        "title": "最高价",
        "key": "f15",
        "name": "Hign"
    },
    {
        "title": "最低价",
        "key": "f16",
        "name": "Low"
    },
    {
        "title": "昨收价",
        "key": "f18",
        "name": "PreviousClose"
    },
    {
        "title": "总市值(美元)",
        "key": "f20",
    },
    {
        "title": "市盈率",
        "key": "f115",
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
        "key": "ORG_EN_ABBR",
    },
    {
        "title": "中文名称",
        "key": "ORG_NAME",
    },
    # {
    #     "title": "注册地",
    #     "key": "REG_PLACE",
    # },
    {
        "title": "注册地址",
        "key": "REG_ADDRESS",
    },
    {
        "title": "成立日期",
        "key": "FOUND_DATE",
    },
    {
        "title": "所属行业",
        "key": "BELONG_INDUSTRY",
    },
    {
        "title": "主席",
        "key": "CHAIRMAN",
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
        "title": "电话号码",
        "key": "ORG_TEL",
    },
    {
        "title": "传真号码",
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
        "key": "SECURITY_CODE",
    },
    # {
    #     "title": "证券简称",
    #     "key": "SECURITY_NAME_ABBR",
    # },
    {
        "title": "上市日期",
        "key": "LISTING_DATE",
    },
    {
        "title": "证券类型",
        "key": "SECURITY_TYPE",
    },
    {
        "title": "上市场所",
        "key": "TRADE_MARKET",
    },
    # {
    #     "title": "板块",
    #     "key": "BOARD",
    # },
    # {
    #     "title": "最新交易单位（每手股数）",
    #     "key": "TRADE_UNIT",
    # },
    {
        "title": "ISIN",
        "key": "ISIN_CODE",
    },
    {
        "title": "每股面值",
        "key": "PAR_VALUE",
    },
    {
        "title": "ADS折算比",
        "key": "CONVERT_RATIO",
    },
    {
        "title": "年结日",
        "key": "YEAR_SETTLE_DAY",
    },
]
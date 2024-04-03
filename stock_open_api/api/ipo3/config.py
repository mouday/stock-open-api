# -*- coding: utf-8 -*-
"""
@File    : config.py
@Date    : 2024-04-03
"""

COMPANY_INFO_KEY_MAP = {
    "股票名称": "stock_name",
    "股票代码": "stock_code",
    "所属行业": "industry",
    "今开": "open_price",
    "最高": "high_price",
    "平均价": "average_price",
    "市盈率": "pe_ratio",
    "成交量": "volume",
    "总市值": "total_market_value",
    "昨收": "prev_close_price",
    "最低": "low_price",
    "换手率": "turnover_rate",
    "市净率": "pb_ratio",
    "成交额": "turnover",
    "流通市值": "circular_market_value",
    "公司名称": "company_name",
    "公司网址": "company_website",
    "公司电话": "company_phone",
    "董秘": "company_secretary",
    "董秘Email": "company_secretary_email",
    "董秘电话": "company_secretary_phone",
    "法人": "legal_representative",
    "主办券商": "broker",
    "交易方式": "transaction_method",
    "挂牌日期": "listing_date",
    "成立日期": "establish_date",
    "做市日期": "making_date",
    "注册资本": "registered_capital",
    "所属地区": "area",
    "办公地址": "company_address",
    "公司简介": "company_introduction",
    "主营业务": "main_business",
    "经营范围": "business_scope",
    "融资状态": "financing_status",
    "实际募资净额": "financing_actual_net_amount",
    "融资成功率": "financing_success_rate",
    "融资排名": "financing_ranking",
    "股本": {
        'value': "equity",
        'children': {
            "总股本": "total_equity",
            "流通股本": "flow_equity",
            "股东户数": "shareholders_number",
            "统计日期": "date"
        }
    },
    "股东结构": {
        'value': "shareholder_list",
        'children': {
            "股东名称": "shareholder_name",
            "持股数": "shares_number",
            "持股比例": "shareholding_ratio"
        }
    },
    "高管介绍": {
        'value': "manager_list",
        'children': {
            "姓名": "name",
            "职位": "position",
            "最高学历": "highest_education",
            "任期开始日期": "term_start_date",
            "简介": "introduction"
        }
    },
    "新闻资讯": {
        'value': "news_list",
        'children': {
            "标题": "title",
            "摘要": "summary",
            "地址": "url",
            "来源": "source",
            "时间": "publish_time"
        }
    }
}

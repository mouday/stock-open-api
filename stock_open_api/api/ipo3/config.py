# -*- coding: utf-8 -*-
"""
@File    : config.py
@Date    : 2024-04-03
"""

COMPANY_INFO_KEY_MAP = {
    "股票名称": "stock_name",
    "股票代码": "stock_code",
    "最新价": "last_price",
    "涨跌额": "change_value",
    "涨跌幅": "change_rate",
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

# 利润表
# ref:
# 财务实用英语词汇：利润表和资产负债表 https://zhuanlan.zhihu.com/p/34316347
INCOME_STATEMENT_KEY_MAP = {
    "利润表": "income_statement",
    "报告期": "report_date",
    "营业总收入": "total_sales_revenue",
    "营业收入": "sales_revenue",
    "营业总成本": "total_sales_cost",
    "营业成本": "sales_cost",
    "营业税金及附加": "additional_tax",
    "销售费用": "selling_expenses",
    "管理费用": "management_expenses",
    "财务费用": "financial_expenses",
    "资产减值损失": "asset_impairment_loss",
    "加:投资收益": "investment_income",
    "其中:对联营企业和合营企业的投资收益": "investment_income_from_associates_and_joint_ventures",
    "营业利润": "sales_profit",
    "加:营业外收入": "non_operating_income",
    "减:营业外支出": "non_operating_expenses",
    "其中:非流动资产处置净损失": "net_loss_from_disposal_of_non_current_assets",
    "利润总额": "total_profit",
    "减:所得税费用": "income_tax_expenses",
    "净利润": "net_profit",
    "归属于母公司股东的净利润": "net_profit_attributable_to_shareholders_of_the_parent_company",
    "综合收益总额": "total_comprehensive_income",
    "归属于母公司所有者的综合收益总额": "total_comprehensive_income_attributable_to_the_owners_of_the_parent_company",
    "基本每股收益": "basic_earnings_per_share",
    "公告日期": "publish_date"
}

# 资产负债表
# ref: https://zhuanlan.zhihu.com/p/34316347
# https://mp.weixin.qq.com/s/5gKV0I7TxgCapUacNaN0OQ
# https://mp.weixin.qq.com/s/aHWVOgtQd2dQzdIdvMe6vQ
# 干货分享收藏—财务术语中英文对照表 https://zhuanlan.zhihu.com/p/633517119
BALANCE_SHEET_KEY_MAP = {
    "资产负债表": "balance_sheet",
    "报告期": "report_date",
    "货币资金": "cash_and_bank",
    "应收票据": "notes_receivable",
    "应收账款": "accounts_receivable",
    "预付款项": "advance_payment",
    "其他应收款": "other_receivable",
    "存货": "inventory",
    "其他流动资产": "other_current_assets",
    "流动资产合计": "total_current_assets",
    "可供出售金融资产": "financial_assets_available_for_sale",
    "长期股权投资": "long_term_equity_investments",
    "投资性房地产": "investment_real_estate",
    "固定资产": "fixed_asset",
    "无形资产": "intangible_asset",
    "长期待摊费用": "long_term_deferred_expenses",
    "递延所得税资产": "deferred_income_tax_asset",
    "非流动资产合计": "non_current_asset",
    "资产总计": "total_assets",
    "应付票据": "notes_payable",
    "应付账款": "accounts_payable",
    "预收款项": "deposit_received",
    "应付职工薪酬": "salary_payable",
    "应交税费": "tax_payable",
    "应付股利": "dividend_payable",
    "其他应付款": "other_payable",
    "流动负债合计": "total_current_liabilities",
    "其他非流动负债": "other_non_current_liabilities",
    "非流动负债合计": "total_non_current_liabilities ",
    "负债合计": "total_liabilities",
    "实收资本(或股本)": "paid_in_capital",
    "资本公积": "capital_reserve",
    "盈余公积": "earned_surplus",
    "未分配利润": "undistributed_profit",
    "外币报表折算差额": "translation_difference_of_foreign_currency_statements",
    "归属于母公司股东权益合计": "total_equity_attributable_to_shareholders_of_the_parent_company",
    "股东权益合计": "total_equity",
    "负债和股东权益合计": "total_liabilities_and_shareholder_equity",
    "公告日期": "publish_date"
}

# 现金流量表
# ref: https://baijiahao.baidu.com/s?id=1727960591437597309
CASH_FLOW_STATEMENT_KEY_MAP = {
    "现金流量表": "cash_flow_statement",
    "报告期": "report_date",
    "销售商品、提供劳务收到的现金": "cash_received_from_goods_and_services",
    "收到的税费返还": "refunds_of_taxes",
    "收到其他与经营活动有关的现金": "other_cash_receipts_relating_to_operating_activities",
    "经营活动现金流入小计": "sub_total_of_cash_inflows_from_operating_activities",
    "购买商品、接受劳务支付的现金": "cash_paid_for_goods_and_services",
    "支付给职工以及为职工支付的现金": "cash_paid_to_and_on_behalf_of_employees",
    "支付的各项税费": "payments_of_all_types_of_taxes",
    "支付其他与经营活动有关的现金": "other_cash_payments_relating_to_operating_activities",
    "经营活动现金流出小计": "sub_total_of_cash_outflows_to_operating_activities",
    "经营活动产生的现金流量净额": "net_cash_flows_from_operating_activities",
    "收回投资收到的现金": "cash_received_from_return_of_investment",
    "取得投资收益收到的现金": "cash_received_from_return_on_investment",
    "处置固定资产、无形资产和其他长期资产收回的现金净额": "net_cash_received_from_the_sale_of_fixed_assets_intangible_assets_and_other_long_term_assets",
    "处置子公司及其他营业单位收到的现金净额": "net_cash_received_from_disposal_of_subsidiaries_and_other_operating_units",
    "收到其他与投资活动有关的现金": "other_cash_receipts_relating_to_investing_activities",
    "投资活动现金流入小计": "sub_total_of_cash_inflows_from_investing_activities",
    "购建固定资产、无形资产和其他长期资产支付的现金": "cash_paid_to_acquire_fixed_assets_intangible_assets_and_other_long_term_assets",
    "投资活动现金流出小计": "sub_total_of_cash_outflows_to_investing_activities",
    "投资活动产生的现金流量净额": "net_cash_flows_from_investing_activities",
    "筹资活动现金流入小计": "sub_total_of_cash_inflows_from_financing_activities",
    "筹资活动现金流出小计": "sub_total_of_cash_outflows_to_financing_activities",
    "汇率变动对现金的影响": "effect_of_changes_in_foreign_exchange_rate_on_cash",
    "现金及现金等价物净增加额": "net_increase_in_cash_and_cash_equivalents",
    "期初现金及现金等价物余额": "opening_balance_of_cash_and_cash_equivalents",
    "期末现金及现金等价物余额": "closing_balance_of_cash_and_cash_equivalents",
    "净利润": "net_profit",
    "加: 资产减值准备": "asset_impairment_provision",
    "固定资产折旧、油气资产折耗、生产性生物资产折旧": "depreciation_of_fixed_assets_depletion_of_oil_and_gas_assets_and_depreciation_of_productive_biological_assets",
    "无形资产摊销": "amortization_of_intangible_assets",
    "长期待摊费用摊销": "amortization_of_long_term_prepayment",
    "处置固定资产、无形资产和其他长期资产的损失": "losses_on_disposal_of_fixed_assets_intangible_assets_and_other_long_term_assets",
    "财务费用": "financial_expenses",
    "投资损失": "investment_loss",
    "递延所得税资产减少": "decrease_in_deferred_income_tax_assets",
    "存货的减少": "decrease_in_inventories",
    "经营性应收项目的减少": "decrease_in_operating_payables",
    "经营性应付项目的增加": "increase_in_operating_payables",
    "其他": "other",
    "现金的期末余额": "cash_at_end_of_period",
    "减:现金的期初余额": "cash_at_beginning_of_period",
    "公告日期": "publish_date"
}

# 财务分析表
# ref: https://fanyi.baidu.com/mtpe-individual/multimodal#/
FINANCIAL_ANALYSIS_KEY_MAP = {
    "财务分析": "financial_analysis",
    "报告期": "report_date",
    "每股收益-基本(元)": "earnings_per_share_of_base",
    "每股收益-稀释(元)": "earnings_per_share_of_dilute",
    "每股收益-扣除/基本(元)": "earnings_per_share_of_deduction_division_base",
    "每股收益-扣除/稀释(元)": "earnings_per_share_of_deduction_division_dilute",
    "每股净资产(元)": "net_asset_value_per_share",
    "每股经营活动产生的现金流量净额(元)": "net_cash_flow_generated_from_operating_activities_per_share",
    "每股收益-期末股本摊薄(元)": "earnings_per_share_of_diluted_share_capital_at_the_end_of_the_period",
    "每股营业总收入(元)": "total_operating_income_per_share",
    "每股营业收入(元)": "operating_income_per_share",
    "每股息税前利润(元)": "pre_tax_profit_per_dividend",
    "每股资本公积(元)": "capital_reserve_per_share",
    "每股盈余公积(元)": "surplus_reserves_per_share",
    "每股未分配利润(元)": "undistributed_profit_per_share",
    "每股留存收益(元)": "retained_earnings_per_share",
    "每股现金流量净额(元)": "net_cash_flow_per_share",
    "每股企业自由现金流量(元)": "free_cash_flow_per_share_of_enterprise",
    "每股股东自由现金流量(元)": "free_cash_flow_per_share_of_shareholder",
    "净资产收益率-摊薄(%)": "return_on_equity_diluted",
    "净资产收益率-加权(%)": "return_on_equity_weighted",
    "净资产收益率-扣除/摊薄(%)": "return_on_equity_deduction_division_dilution",
    "净资产收益率-扣除/加权(%)": "return_on_equity_deduction_division_weighted",
    "净资产收益率-年化(%)": "return_on_equity_annualized",
    "总资产报酬率(%)": "total_asset_return_rate",
    "总资产报酬率-年化(%)": "total_asset_return_rate_annualized",
    "总资产净利率(%)": "net_profit_margin_of_total_assets",
    "总资产净利率-年化(%)": "net_profit_margin_of_total_assets_annualized",
    "投入资本回报率(%)": "return_on_investment_capital",
    "销售净利率(%)": "sales_net_profit_margin",
    "销售毛利率(%)": "sales_gross_profit_margin",
    "销售成本率(%)": "sales_cost_rate",
    "销售期间费用率(%)": "sales_period_expense_rate",
    "净利润/营业总收入(%)": "net_profit_total_division_operating_income",
    "营业利润/营业总收入(%)": "operating_profit_division_total_operating_income",
    "营业总成本/营业总收入(%)": "total_operating_cost_division_total_operating_income",
    "营业费用/营业总收入(%)": "operating_expenses_division_total_operating_income",
    "管理费用/营业总收入(%)": "management_expenses_division_total_operating_income",
    "财务费用/营业总收入(%)": "financial_expenses_division_total_operating_income",
    "资产减值损失/营业总收入(%)": "asset_impairment_loss_division_total_operating_income",
    "经营活动净收益/利润总额(%)": "net_income_from_operating_activities_division_total_profit",
    "价值变动净收益/利润总额(%)": "value_change_net_income_division_total_profit",
    "营业外支出净额/利润总额(%)": "net_non_operating_expenses_division_total_profit",
    "所得税/利润总额(%)": "income_tax_division_total_profit",
    "扣除非经常性损益的净利润/净利润(%)": "net_profit_after_deducting_non_recurring_gains_and_losses_division_net_profit",
    "资产负债率(%)": "asset_liability_ratio",
    "权益乘数(%)": "equity_multiplier",
    "流动资产/总资产(%)": "current_assets_division_total_assets",
    "非流动资产/总资产(%)": "non_current_assets_division_total_assets",
    "有形资产/总资产(%)": "tangible_assets_division_total_assets",
    "归属母公司股东的权益/全部投入资本(%)": "equity_attributable_to_shareholders_of_the_parent_company_division_total_invested_capital",
    "带息负债/全部投入资本(%)": "interest_bearing_liabilities_division_total_invested_capital",
    "流动负债/负债合计(%)": "current_liabilities_division_total_liabilities",
    "非流动负债/负债合计(%)": "non_current_liabilities_division_total_liabilities",
    "流动比率": "current_ratio",
    "速动比率": "quick_ratio",
    "保守速动比率": "conservative_quick_ratio",
    "产权比率": "property_ownership_ratio",
    "归属母公司股东的权益/负债合计": "equity_attributable_to_shareholders_of_the_parent_company_division_total_liabilities",
    "归属母公司股东的权益/带息债务": "equity_attributable_to_shareholders_of_the_parent_company_division_interest_bearing_debt",
    "有形资产/负债合计": "total_tangible_assets_division_liabilities",
    "有形资产/带息债务": "tangible_assets_division_interest_bearing_debt",
    "有形资产/净债务": "tangible_assets_division_net_debt",
    "息税折旧摊销前利润/负债合计": "profit_before_interest_tax_depreciation_and_amortization_division_total_liabilities",
    "经营活动产生的现金流量净额/负债合计": "net_cash_flow_generated_from_operating_activities_division_total_liabilities",
    "经营活动产生的现金流量净额/带息债务": "net_cash_flow_generated_from_operating_activities_division_interest_bearing_debt",
    "经营活动产生的现金流量净额/流动负债": "net_cash_flow_generated_from_operating_activities_division_current_liabilities",
    "经营活动产生的现金流量净额/净债务": "net_cash_flow_generated_from_operating_activities_division_net_debt",
    "已获利息倍数": "received_interest_multiple",
    "长期债务与营运资金比率": "long_term_debt_to_working_capital_ratio",
    "营业周期(天)": "business_cycle",
    "存货周转天数(天)": "inventory_turnover_days",
    "应收账款周转天数(天)": "accounts_receivable_turnover_days",
    "存货周转率(次)": "inventory_turnover",
    "应收账款周转率(次)": "accounts_receivable_turnover_rate",
    "流动资产周转率(次)": "current_asset_turnover_rate",
    "固定资产周转率(次)": "fixed_asset_turnover_rate",
    "总资产周转率(次)": "total_asset_turnover_rate",
    "营业总收入同比增长率(%)": "yoy_growth_rate_of_total_operating_revenue",
    "营业收入同比增长率(%)": "yoy_growth_rate_of_operating_revenue",
    "销售商品提供劳务收到的现金/营业收入(%)": "cash_received_from_selling_goods_and_providing_services_division_operating_income",
    "经营活动产生的现金流量净额/营业收入(%)": "net_cash_flow_generated_from_operating_activities_division_operating_income",
    "经营活动产生的现金流量净额/经营活动净收益(%)": "net_cash_flow_generated_from_operating_activities_division_net_income_from_operating_activities",
    "资本支出/折旧摊销(%)": "capital_expenditure_division_depreciation_and_amortization"
}

# 犀牛之心-募资明细
STOCK_FUND_KEY_MAP = {
    "募资日期": "fund_date",
    "募资类型": "fund_type",
    "募集资金": "fund_money",
    "增发数量": "additional_issuance_quantity",
    "增发价格": "additional_issuance_price",
    "投资人列表": {
        'value': "investor_list",
        'children': {
            "投资者": "investor",
            "类型": "investor_type",
            "是否为公司高管": "is_company_executive",
            "持股数": "number_of_shares_held",
            "投资额（元）": "investment_amount",
            "锁定状态": "locked_state"
        }
    }
}

# 犀牛之心-交易明细
STOCK_TRADE_KEY_MAP = {
    "交易日期": "trade_date",
    "总成交额（元）": "total_trade_amount",
    "成交价格（元）": "trade_price",
    "成交数量（股）": "trade_quantity",
    "买方账号名称": "buyer_name",
    "买方主办券商": "buyer_broker",
    "卖方账号名称": "seller_name",
    "卖方主办券商": "seller_broker"
}

# 犀牛之心-最新公告-大事提醒
STOCK_EVENT_KEY_MAP = {
    "事件日期": "event_date",
    "事件类型": "event_type",
    "事件标题": "title"
}

# 犀牛之心-最新公告-最新公告
STOCK_NOTICE_KEY_MAP = {
    "数据id": "id",
    "公告标题": "title",
    "公告文件": "down_url",
    "公告原始文件": "original_file_url",
    "发布日期": "time",
    "公告详情": "detail_url"
}

# 犀牛之心-最新公告-定增计划
STOCK_SURVEY_KEY_MAP = {
    "融资进度": "financing_progress",
    "融资金额": "financing_money",
    "出让股份": "transfer_of_shares",
    "每股价格": "price_per_share",
    "最新公告日": "latest_announcement_date",
    "预案公告日": "plan_announcement_date",
    "董秘": "company_secretary",
    "董秘电话": "company_secretary_phone",
    "董秘邮箱": "company_secretary_email",
    "行业分类": "industry",
    "主办券商": "broker",
    "增发对象": "additional_issuance_target",
    "增发目的": "purpose_of_issuance"
}

# 犀牛之心-持股成本-做市商持股成本
STOCK_BROKER_KEY_MAP = {
    "做市商": "broker",
    "初始库存": "initial_stock",
    "初始价格": "initial_price"
}

# 犀牛之心-质押信息-质押企业详情
STOCK_PLEDGE_DATA_KEY_MAP = {
    "累计质押": "pledge_total",
    "质押股东": "pledge_shareholders",
    "质权人": "pledge_pledgee"
}

# 犀牛之心-质押信息-质押贷款记录
STOCK_PLEDGE_LOAN_RECORD_KEY_MAP = {
    "股东名称": "shareholder_name",
    "质押日期": "pledge_date",
    "贷款金额": "loan_amount",
    "质权人": "pledgee",
    "质押占总股比": "pledge_to_total_ratio",
    "质押占所持股比": "pledge_to_equity_ratio",
    "质押率": "pledge_rate",
    "质押股数": "pledged_shares",
    "质押起初日": "pledge_start_date",
    "质押截止日": "pledge_end_date",
    "质押说明": "pledge_description"
}


# 犀牛之心-研报
STOCK_REPORT_KEY_MAP = {
    "研报标题": "title",
    "详情地址": "detail_url",
    "发布日期": "publish_date"
}

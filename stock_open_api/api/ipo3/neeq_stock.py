# -*- coding: utf-8 -*-
"""
@File    : neeq_stock.py
@Date    : 2024-04-02
"""
import re

from parsel import Selector

from stock_open_api.api.ipo3 import config
from stock_open_api.utils import request_util, table_util, convert_util
from stock_open_api.log import logger


def get_company_info(stock_code, proxies=None, english_key=False, timeout=3):
    """
    获取股票详情信息

    页面地址：https://www.ipo3.com/company-show/stock_code-430510.html

    :param english_key:
    :param proxies:
    :param stock_code: 股票代码
    :return:

    eg:
    {
      "股票名称": "丰光精密",
      "股票代码": "430510",
      "最新价": "17.32",
      "涨跌额": "-1.18",
      "涨跌幅": "-6.38%",
      "所属行业": "机械基础件",
      "今开": "19.89",
      "最高": "19.92",
      "平均价": "18.96",
      "市盈率": "33.26",
      "成交量": "2.76万",
      "总市值": "24.34亿",
      "昨收": "19.79",
      "最低": "18.47",
      "换手率": "4.38%",
      "市净率": "6.19%",
      "成交额": "5225.06万",
      "流通市值": "11.64亿",
      "公司名称": "青岛丰光精密机械股份有限公司",
      "公司网址": "http://www.qdfg.cn",
      "公司电话": "0532-87273590",
      "董秘": "吕冬梅",
      "董秘Email": "fgzq@fengguang.net.cn",
      "董秘电话": "0532-87273528",
      "法人": "李军",
      "主办券商": "中信证券",
      "交易方式": "集合竞价",
      "挂牌日期": "1970-01-01",
      "成立日期": "2001-07-19",
      "做市日期": "2015-07-28",
      "注册资本": "13158.1378 万元",
      "所属地区": "山东省-青岛市",
      "办公地址": "山东省青岛市胶州市胶州湾工业园太湖路2号",
      "公司简介": "青岛丰光精密机械股份有限公司是一家以高精密部品的加工和组装,以及铝制品铸造为核心技术和核心产品的国家级高新技术企业,先后通过了国际质量管理体系ISO9001认证和汽车行业生产件与相关服务件质量管理体系IATF16949认证等管理体系。2021年11月15日成为北交所首批上市企业。公司现有三个生产工厂,并在美国设立全资子公司,拥有数百台国外进口品牌数控加工中心、数控车床、高精度磨床、压铸机等加工、压铸及检测设备,拥有恒温恒湿的欧标标准化生产车间。随着业务的不断扩大及企业的高速发展,公司在中国——上海合作组织地方经贸合作示范区,正在建设中的上合工厂,占地10万平方米。公司产品覆盖半导体、工业自动化、汽车、轨道交通等众多领域。以高精密、高品质、高稳定性的产品赢得了众多国际各行业顶尖制造商的认可,并成为长期战略合作伙伴,如THK集团、安川电机、埃地沃兹、费斯托、山洋电机、盖茨集团、中国中车、阿尔斯通、均胜、日本电产岱高公司以及阿特拉斯等。公司在经营管理过程中,注重技术研发能力的提升,公司先后被评为国家级高新技术企业、青岛市企业技术中心、山东省企业技术中心、青岛市“专精特新”示范企业等。公司通过不断的学习和创新,有较高的自主开发技能,如四轴机器人、六轴机器人,并成功研制开发了多款适合不同行业要求的系列产品等。公司坚持“客户导向”的理念,在精密机械加工件和压铸件方面,根据下游不同行业客户的要求研发、设计产品,并实施最优的生产工序、加工方法及每道工序的加工标准,并进行精细化管理生产,且在工艺技术、生产设备技术先进程度和操控经验等方面处于国内领先水平。公司自成立以来一直秉承取之社会,回报于社会的企业文化理念,除了立足生产、发展企业外,一直积极参与各类社会公益活动,如抗震救灾捐助、小草基金公益捐助、孤寡老人救助、为伤残人士提供就业岗位、帮扶困难员工家庭等行动,希望通过丰光人的点滴行动,传递爱心,帮助更多需要帮助的人。",
      "主营业务": "半导体领域、工业自动化领域、汽车领域、轨道交通领域精密零部件的研发、生产与销售。",
      "经营范围": "精密轴承及各种电机轴的制造，各种精密机械零部件的加工、组装；铝合金部件及锌合金部件压铸成型及加工，金属制品模具设计、制造。（依法须经批准的项目，经相关部门批准后方可开展经营活动）。",
      "融资状态": "定增中",
      "实际募资净额": "4,966.95万",
      "融资成功率": "100.00%",
      "融资排名": "1/14",
      "股本": [
        {
          "总股本": "1.32亿 股",
          "流通股本": "6,292.64万 股",
          "统计日期": "2023-09-30",
          "股东户数": "4,022 户"
        }
      ],
      "股东结构": [
        {
          "股东名称": "青岛丰光投资管理有限公司",
          "持股数": "7,329.50万 股",
          "持股比例": "55.70%"
        }
      ],
      "高管介绍": [
        {
          "姓名": "李军",
          "职位": "董事长",
          "最高学历": "本科",
          "任期开始日期": "2019-09",
          "简介": "李军先生:1970年出生,民建会员,中国国籍,无境外居留权,本科学历。2001年10月至2013年9月,先后担任有限公司副董事长兼总经理董事长兼总经理。2013年9月至2016年3月,担任股份公司董事长兼总经理。2016年4月至今担任股份公司董事长。"
        }
      ],
      "新闻资讯": [
        {
          "标题": "【北交所收评】盘面震荡冲高，北证50大涨近2%，电力、锂电池板块涨幅居前，亿能电力封涨停",
          "摘要": "犀牛之星3月11日讯，今日北交所整体呈现低开高走趋势，午后盘面放量冲高，北证50大涨近2%；受AI算力高耗电量推动，电力板块集体高涨，其中亿能电力（837046）封涨停、灿能电力（870299）涨逾13%；受摩根士丹利上调宁德时代股价提振，午后锂电池概念股震荡走强，天宏锂电（873152）涨逾22%、力王股份（831627）涨逾15%、长虹能源（836239）涨逾13%；次新股铁拓机械（873706）跌逾12%。",
          "地址": "https://www.ipo3.com/company-news/id-1428579.html",
          "来源": "犀牛之星",
          "时间": "2024-03-11 15:24:28"
        }
      ]
    }

    """
    url = "https://www.ipo3.com/company-show/stock_code-{stock_code}.html".format(stock_code=stock_code)

    logger.info("url: %s", url)

    res = request_util.get(url, proxies=proxies, timeout=timeout)

    sel = Selector(text=res.text)
    stock_name = sel.css('#stockName::text').extract_first('').strip()
    cur_price = sel.css('.company-detail .cur-price span::text').extract_first('').strip()
    range_num = sel.css('.company-detail .range-num::text').extract_first('').strip()
    range_percent = sel.css('.company-detail .range-percent::text').extract_first('').strip()

    data = {
        '股票名称': stock_name,
        '股票代码': stock_code,
        '最新价': cur_price,
        '涨跌额': range_num,
        '涨跌幅': range_percent,
    }

    # 所属行业
    key, value = sel.css('.industry').xpath('string(.)').extract_first('').split('：')
    data[key.strip()] = value.strip()

    # 市值
    for item in sel.css('.exponent .item'):
        key = item.css('span::text').extract_first('')
        value = item.css('strong::text').extract_first('')
        data[key.strip(':').strip().replace(' ', '')] = value.strip()

    # 基本信息
    for item in sel.css('.company-sheet .sheet-item'):
        key = item.css('span::text').extract_first('').strip('：').strip()
        value = item.css('strong::attr(title)').extract_first('').strip()
        if key == '所属地区':
            value = value.replace(' ', '')

        data[key] = value

    # 定增融资
    for row in sel.css('.strategy-info .strategy-item'):
        key = row.css('.strategy-tit::text').extract_first('').strip()
        value = row.css('.strategy-status::text,span::text').extract_first('').strip()
        if key == '融资排名':
            value = value.replace(' ', '')

        data[key] = value

    #
    for key, value in zip(sel.css('.company-total .lc-title span::text').extract(), sel.css('.company-total .lc-main')):
        key = key.strip()

        if key in ['公司简介', '主营业务', '经营范围']:
            data[key] = value.css('::text').extract_first('').strip()
        elif key in ['股本', '股东结构']:
            items = table_util.parse_table(value)

            if key == '股本':
                lst = []
                for x in items:
                    r = {}
                    for k, v in x.items():
                        # 股东户数 (2022-06-30)
                        ret = re.search('\d{4}-\d{2}-\d{2}', k)
                        if ret:
                            date = ret.group(0)
                            r['统计日期'] = date
                            r['股东户数'] = v
                        else:
                            r[k] = v
                    lst.append(r)
                data[key] = lst
            else:
                data[key] = items
        elif key == '高管介绍':
            items = parse_introduce_table(value)
            for item in items:
                # eg: 2013-09 => 2013-09-01
                if item['任期开始日期'] and len(item['任期开始日期']) == 7:
                    item['任期开始日期'] = item['任期开始日期'] + '-01'

            data[key] = items

        elif key == '新闻资讯':
            data[key] = parse_news_list(value)

    # replace '-' to ''
    for key in data:
        if isinstance(data[key], str):
            if data[key] == '-':
                data[key] = ''

    if english_key:
        return convert_util.convert_key(config.COMPANY_INFO_KEY_MAP, data)
    else:
        return data


def parse_introduce_table(sel: Selector):
    """
    解析高管介绍
    :param sel:
    :return:
    """
    lst = []

    # 解析表头
    headers = [x.xpath('string(.)').extract_first('').strip() for x in sel.css('thead th')]

    # 解析内容
    for row, info in zip(sel.css('tbody tr.J_click'), sel.css('tbody tr.info-detail')):
        item = {}

        for key, value in zip(headers, row.css("td")):
            if key == '简介':
                item[key] = info.xpath('string(.)').extract_first('').strip()
            else:
                item[key] = value.xpath('string(.)').extract_first('').strip()

        lst.append(item)

    return lst


def parse_news_list(value: Selector):
    """
    解析文章列表
    :param value:
    :return:
    """
    lst = []
    for row in value.css('.news-item'):
        title = row.css('h3 a::text').extract_first('').strip()
        href = row.css('h3 a::attr(href)').extract_first('').strip()
        summary = row.css('p ::text').extract_first('').strip()

        item = {
            '标题': title,
            '摘要': summary,
            '地址': "https://www.ipo3.com" + href
        }

        for x in row.css('.about span::text').extract():
            key, value = x.split('：')
            item[key.strip()] = value.strip()

        lst.append(item)

    return lst


def get_income_statement_list(stock_code, date_type='年报', english_key=False):
    """
    获取利润表
    eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001.html#content
    :param stock_code: str 股票代码
    :param date_type: str 可选值：年报/中报/一季报/三季报
    :param english_key: bool
    :return:
    [
      {
        "利润表": "2022年报",
        "报告期": "2022-12-31",
        "营业总收入": "2.52亿",
        "营业收入": "2.52亿",
        "营业总成本": "2.21亿",
        "营业成本": "1.74亿",
        "营业税金及附加": "187.87万",
        "销售费用": "833.65万",
        "管理费用": "2,350.09万",
        "财务费用": "-34.44万",
        "资产减值损失": "-123.86万",
        "加:投资收益": "2.07万",
        "其中:对联营企业和合营企业的投资收益": "",
        "营业利润": "7,241.32万",
        "加:营业外收入": "727.49万",
        "减:营业外支出": "72.48万",
        "其中:非流动资产处置净损失": "",
        "利润总额": "7,896.34万",
        "减:所得税费用": "577.89万",
        "净利润": "7,318.44万",
        "归属于母公司股东的净利润": "7,318.44万",
        "综合收益总额": "7,336.21万",
        "归属于母公司所有者的综合收益总额": "7,336.21万",
        "基本每股收益": "0.56",
        "公告日期": "2022-12-31"
      }
    ]
    """

    date_type_map = {
        '年报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-001.html#content',
        '中报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-002.html#content',
        '一季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-003.html#content',
        '三季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-004.html#content'
    }

    # eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001.html#content
    url = date_type_map[date_type].format(stock_code=stock_code)
    res = request_util.get(url)
    sel = Selector(text=res.text)

    items = parse_finance_table(sel)

    if english_key:
        items = [convert_util.convert_key(config.INCOME_STATEMENT_KEY_MAP, item) for item in items]

    return items


def get_balance_sheet_list(stock_code, date_type='年报', english_key=False):
    """
    获取资产负债表
    eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-debt.html#content
    :param stock_code: str 股票代码
    :param date_type: str 可选值：年报/中报/一季报/三季报
    :param english_key: bool
    :return:
    [
      {
        "资产负债表": "2022年报",
        "报告期": "2022-12-31",
        "货币资金": "5,299.30万",
        "应收票据": "",
        "应收账款": "6,654.62万",
        "预付款项": "210.41万",
        "其他应收款": "61.03万",
        "存货": "4,726.91万",
        "其他流动资产": "235.83万",
        "流动资产合计": "1.73亿",
        "可供出售金融资产": "",
        "长期股权投资": "",
        "投资性房地产": "",
        "固定资产": "1.90亿",
        "无形资产": "3,358.86万",
        "长期待摊费用": "",
        "递延所得税资产": "41.86万",
        "非流动资产合计": "3.30亿",
        "资产总计": "5.03亿",
        "应付票据": "",
        "应付账款": "2,107.15万",
        "预收款项": "",
        "应付职工薪酬": "330.19万",
        "应交税费": "70.60万",
        "应付股利": "",
        "其他应付款": "102.60万",
        "流动负债合计": "5,405.74万",
        "其他非流动负债": "",
        "非流动负债合计": "5,596.92万",
        "负债合计": "1.10亿",
        "实收资本(或股本)": "1.32亿",
        "资本公积": "8,263.42万",
        "盈余公积": "2,933.31万",
        "未分配利润": "1.49亿",
        "外币报表折算差额": "",
        "归属于母公司股东权益合计": "3.93亿",
        "股东权益合计": "3.93亿",
        "负债和股东权益合计": "5.03亿",
        "公告日期": "2022-12-31"
      }
    ]
    """

    date_type_map = {
        '年报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-001-type-debt.html#content',
        '中报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-002-type-debt.html#content',
        '一季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-003-type-debt.html#content',
        '三季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-004-type-debt.html#content'
    }

    # eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-debt.html#content
    url = date_type_map[date_type].format(stock_code=stock_code)
    res = request_util.get(url)
    sel = Selector(text=res.text)

    items = parse_finance_table(sel)

    if english_key:
        items = [convert_util.convert_key(config.INCOME_STATEMENT_KEY_MAP, item) for item in items]

    return items


def get_cash_flows_statement_list(stock_code, date_type='年报', english_key=False):
    """
    获取现金流量表
    eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-cash.html#content
    :param stock_code: str 股票代码
    :param date_type: str 可选值：年报/中报/一季报/三季报
    :param english_key: bool
    :return:
    [
      {
        "现金流量表": "2022年报",
        "报告期": "2022-12-31",
        "销售商品、提供劳务收到的现金": "2.68亿",
        "收到的税费返还": "733.11万",
        "收到其他与经营活动有关的现金": "1,085.65万",
        "经营活动现金流入小计": "2.86亿",
        "购买商品、接受劳务支付的现金": "1.65亿",
        "支付给职工以及为职工支付的现金": "5,186.84万",
        "支付的各项税费": "564.16万",
        "支付其他与经营活动有关的现金": "688.15万",
        "经营活动现金流出小计": "2.29亿",
        "经营活动产生的现金流量净额": "5,675.70万",
        "收回投资收到的现金": "",
        "取得投资收益收到的现金": "2.07万",
        "处置固定资产、无形资产和其他长期资产收回的现金净额": "4,189.57万",
        "处置子公司及其他营业单位收到的现金净额": "",
        "收到其他与投资活动有关的现金": "1,000.00万",
        "投资活动现金流入小计": "5,191.64万",
        "购建固定资产、无形资产和其他长期资产支付的现金": "1.62亿",
        "投资活动现金流出小计": "1.73亿",
        "投资活动产生的现金流量净额": "-1.21亿",
        "筹资活动现金流入小计": "7,643.50万",
        "筹资活动现金流出小计": "1,068.14万",
        "汇率变动对现金的影响": "-5.71万",
        "现金及现金等价物净增加额": "138.34万",
        "期初现金及现金等价物余额": "5,092.93万",
        "期末现金及现金等价物余额": "5,231.27万",
        "净利润": "7,318.44万",
        "加: 资产减值准备": "123.86万",
        "固定资产折旧、油气资产折耗、生产性生物资产折旧": "1,668.24万",
        "无形资产摊销": "84.65万",
        "长期待摊费用摊销": "1.92万",
        "处置固定资产、无形资产和其他长期资产的损失": "-3,945.93万",
        "财务费用": "101.14万",
        "投资损失": "-2.07万",
        "递延所得税资产减少": "-11.12万",
        "存货的减少": "-442.89万",
        "经营性应收项目的减少": "-695.99万",
        "经营性应付项目的增加": "863.24万",
        "其他": "",
        "现金的期末余额": "5,231.27万",
        "减:现金的期初余额": "5,092.93万",
        "公告日期": "2022-12-31"
      }
    ]
    """

    date_type_map = {
        '年报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-001-type-cash.html#content',
        '中报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-002-type-cash.html#content',
        '一季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-003-type-cash.html#content',
        '三季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-004-type-cash.html#content'
    }

    # eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-cash.html#content
    url = date_type_map[date_type].format(stock_code=stock_code)
    res = request_util.get(url)
    sel = Selector(text=res.text)

    items = parse_finance_table(sel)

    if english_key:
        items = [convert_util.convert_key(config.CASH_FLOWS_STATEMENT_KEY_MAP, item) for item in items]

    return items


def get_financial_analysis_list(stock_code, date_type='年报', english_key=False):
    """
    获取财务分析表
    eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-analysis.html#content
    :param stock_code: str 股票代码
    :param date_type: str 可选值：年报/中报/一季报/三季报
    :param english_key: bool
    :return:
    [
      {
        "财务分析": "2022年报",
        "报告期": "2022-12-31",
        "每股收益-基本(元)": "0.56",
        "每股收益-稀释(元)": "0.56",
        "每股收益-扣除/基本(元)": "0.20",
        "每股收益-扣除/稀释(元)": "0.20",
        "每股净资产(元)": "2.99",
        "每股经营活动产生的现金流量净额(元)": "0.43",
        "每股收益-期末股本摊薄(元)": "0.56",
        "每股营业总收入(元)": "1.91",
        "每股营业收入(元)": "1.91",
        "每股息税前利润(元)": "0.60",
        "每股资本公积(元)": "0.63",
        "每股盈余公积(元)": "0.22",
        "每股未分配利润(元)": "1.14",
        "每股留存收益(元)": "1.36",
        "每股现金流量净额(元)": "0.01",
        "每股企业自由现金流量(元)": "-0.52",
        "每股股东自由现金流量(元)": "-0.00",
        "净资产收益率-摊薄(%)": "18.62",
        "净资产收益率-加权(%)": "20.53",
        "净资产收益率-扣除/摊薄(%)": "6.85",
        "净资产收益率-扣除/加权(%)": "7.55",
        "净资产收益率-年化(%)": "20.53",
        "总资产报酬率(%)": "18.41",
        "总资产报酬率-年化(%)": "18.41",
        "总资产净利率(%)": "16.93",
        "总资产净利率-年化(%)": "16.93",
        "投入资本回报率(%)": "18.49",
        "销售净利率(%)": "29.08",
        "销售毛利率(%)": "30.69",
        "销售成本率(%)": "69.31",
        "销售期间费用率(%)": "17.64",
        "净利润/营业总收入(%)": "29.08",
        "营业利润/营业总收入(%)": "28.77",
        "营业总成本/营业总收入(%)": "87.69",
        "营业费用/营业总收入(%)": "3.31",
        "管理费用/营业总收入(%)": "14.46",
        "财务费用/营业总收入(%)": "-0.14",
        "资产减值损失/营业总收入(%)": "-0.49",
        "经营活动净收益/利润总额(%)": "39.23",
        "价值变动净收益/利润总额(%)": "0.01",
        "营业外支出净额/利润总额(%)": "8.30",
        "所得税/利润总额(%)": "7.32",
        "扣除非经常性损益的净利润/净利润(%)": "36.78",
        "资产负债率(%)": "21.87",
        "权益乘数(%)": "1.28",
        "流动资产/总资产(%)": "34.32",
        "非流动资产/总资产(%)": "65.68",
        "有形资产/总资产(%)": "71.37",
        "归属母公司股东的权益/全部投入资本(%)": "83.70",
        "带息负债/全部投入资本(%)": "16.30",
        "流动负债/负债合计(%)": "49.13",
        "非流动负债/负债合计(%)": "50.87",
        "流动比率": "3.19",
        "速动比率": "2.32",
        "保守速动比率": "2.22",
        "产权比率": "0.28",
        "归属母公司股东的权益/负债合计": "3.57",
        "归属母公司股东的权益/带息债务": "5.14",
        "有形资产/负债合计": "3.26",
        "有形资产/带息债务": "4.69",
        "有形资产/净债务": "15.25",
        "息税折旧摊销前利润/负债合计": "0.88",
        "经营活动产生的现金流量净额/负债合计": "0.52",
        "经营活动产生的现金流量净额/带息债务": "0.74",
        "经营活动产生的现金流量净额/流动负债": "1.05",
        "经营活动产生的现金流量净额/净债务": "2.41",
        "已获利息倍数": "129.38",
        "长期债务与营运资金比率": "0.47",
        "营业周期(天)": "188.18",
        "存货周转天数(天)": "94.27",
        "应收账款周转天数(天)": "93.91",
        "存货周转率(次)": "3.82",
        "应收账款周转率(次)": "3.83",
        "流动资产周转率(次)": "1.50",
        "固定资产周转率(次)": "1.50",
        "总资产周转率(次)": "0.58",
        "营业总收入同比增长率(%)": "-4.41",
        "营业收入同比增长率(%)": "-4.41",
        "销售商品提供劳务收到的现金/营业收入(%)": "106.33",
        "经营活动产生的现金流量净额/营业收入(%)": "22.55",
        "经营活动产生的现金流量净额/经营活动净收益(%)": "183.22",
        "资本支出/折旧摊销(%)": "922.48"
      }
    ]
    """

    date_type_map = {
        '年报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-001-type-analysis.html#content',
        '中报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-002-type-analysis.html#content',
        '一季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-003-type-analysis.html#content',
        '三季报': 'https://www.ipo3.com/company-show/stock_code-{stock_code}-tab-finance-date_type-004-type-analysis.html#content'
    }

    # eg: https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-analysis.html#content
    url = date_type_map[date_type].format(stock_code=stock_code)
    res = request_util.get(url)
    sel = Selector(text=res.text)

    items = parse_finance_table(sel)

    if english_key:
        items = [convert_util.convert_key(config.FINANCIAL_ANALYSIS_KEY_MAP, item) for item in items]

    return items


def parse_finance_table(sel):
    headers = sel.css('.finance-tab tr th').xpath("string(.)").extract()
    headers = [header.strip() for header in headers]

    # n x 4 的矩阵
    rows = []
    for tr in sel.css('.finance-tab tr'):
        row = []
        for td in tr.css('td'):
            value = td.css('::text').extract_first('').strip()
            # replace empty value
            if value == '-':
                value = ''
            row.append(value)

        rows.append(row)

    if not rows:
        return []

    # 二维矩阵 转 list[dict]
    items = []
    for idx in range(len(rows[0])):
        values = [row[idx] for row in rows]
        item = dict(zip(headers, values))
        items.append(item)

    return items

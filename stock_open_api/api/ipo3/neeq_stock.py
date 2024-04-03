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


def get_company_info(stock_code, english_key=False):
    """
    获取股票详情信息

    页面地址：https://www.ipo3.com/company-show/stock_code-430510.html

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

    res = request_util.get(url)

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


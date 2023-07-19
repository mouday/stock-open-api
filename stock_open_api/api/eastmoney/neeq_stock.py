# -*- coding: utf-8 -*-
"""
@File    : neeq_stock.py
@Date    : 2023-07-17
新三板相关接口
"""

import json

from parsel import Selector

from stock_open_api.api.eastmoney import hk_stock_config, neeq_stock_config
from stock_open_api.items.list_item import ListItem
from stock_open_api.utils import time_util, request_util


def get_list(page=1, size=20):
    """
    新三板列表

    东方财富网 > 行情中心 > 新三板 > 全部
    http://quote.eastmoney.com/center/gridlist.html#neeq_stocks

    :param page: int
    :param size: int

    :return: ListItem

    >>> get_list()
    {
      "total": 6749
      "items": [
        {
          "代码": "872874",
          "名称": "金税股份",
          "最新价": 7.26,
          "涨跌额": 3.63,
          "涨跌幅": 100.0,
          "成交量": 1,
          "成交额": 726.0,
          "昨收": 3.63,
          "今开": 7.26,
          "最高": 7.26,
          "最低": 7.26,
          "委比": -66.5
        }
      ]
    }
    """
    url = 'http://96.push2.eastmoney.com/api/qt/clist/get'

    params = {
        # 'cb': 'jQuery1124022247549421839086_1689658974323',
        'pn': page,  # page num
        'pz': size,  # page size
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'wbp2u': '|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:0 t:81 s:!2052',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111',
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

        for map_item in neeq_stock_config.list_key_map:
            item[map_item['title']] = row.get(map_item['key'])

        items.append(item)

    list_item.items = items
    return list_item


def get_company_info(code):
    """
    新三板 公司资料+证券资料

    eg: http://xinsanban.eastmoney.com/F10/CompanyInfo/Introduction/839499.html

    :param code: str eg: 839499

    :return: dict

    >>> get_company_info('839499')
    {
      "证券代码": "839499.NQ",
      "挂牌日期": "2016-10-27",
      "转让方式": "集合竞价",
      "总股本(万股)": "2630",
      "推荐挂牌券商": "方正证券",
      "证券简称": "西南检测",
      "首次交易日": "2017-05-19",
      "市场分层": "创新层",
      "流通股本(万股)": "2630",
      "持续督导券商": "财通证券",
      "公司全称": "杭州西南检测技术股份有限公司",
      "成立日期": "2007-02-06",
      "实际控制人": "姚文宏,魏川",
      "法人代表": "魏川",
      "公司电话": "0571-88073326",
      "公司邮箱": "hzxnjc@hzsouthwest.com",
      "会计事务所": "中兴华会计师事务所(特殊普通合伙)",
      "主营业务": "建设工程地基基础检测",
      "行业分类": "工业-商业和专业服务",
      "注册地址": "浙江省杭州市拱墅区独城206号6幢",
      "办公地址": "浙江省杭州市拱墅区独城206号6幢",
      "公司简介": "杭州西南检测技术股份有限公司成立于2007年2月,2016年10月10日公司成功登录新三板,是一家国家级高新技术型企业、浙江省科技型中小企业、浙江省“凤凰行动”计划入围企业,杭州市专利示范企业,拱墅区快速成长科技型企业(旭日计划2.0)。公司拥有一支高层次的管理及员工队伍。公司是浙江地区为数不多的能同时承担环境检测及工程检测的第三方检测机构,发起创立了浙江省大健康检测产业创新联盟,致力于打造前端环境检测、中端工程检测、末端大健康检测的链式检测体系,为客户提供综合性的、全生命周期的检测及咨询服务,帮助客户提升品牌价值。公司秉持“始于检测、止于至善”的服务理念,依托于公司在勘察、设计、科研等方面的专业技术优势,打造检测后服务体系,为客户提供“管家式服务”。公司重视创新,设立有技术研究中心及博士后创新工作室,配备有专职研究人员,开展了有针对性的技术研究与开发,在大吨位及复杂条件下的静载抗压测试技术、基坑与隧道智能化远程监测技术等方面具有核心优势。公司将进一步加大投资力度,开展新兴检测业务的孵化培育,不断拓展市场空间。加强横向联合,优化管理模式,提升企业的综合实力,为所有客户提供优质服务。",
      "注册资本(亿元)": "0.2630",
      "组织形式": "民营企业",
      "员工总数": "494",
      "公司董秘": "祝世昌",
      "公司传真": "0571-88080313",
      "律师事务所": "北京康达(杭州)律师事务所"
    }
    """
    base_url = "http://xinsanban.eastmoney.com/F10/CompanyInfo/Introduction/{code}.html"
    url = base_url.format(code=code)

    response = request_util.get(url)

    sel = Selector(text=response.text)
    security_info = sel.css("#security_info li")
    company_info = sel.css("#company_info li")
    rows = security_info + company_info

    item = {}
    for row in rows:
        key = row.css(".company-page-item-left::text").extract_first("").strip()
        value = row.css(".company-page-item-right::text").extract_first("").strip()
        item[key] = value

    return item


if __name__ == '__main__':
    print(json.dumps(get_list().to_dict(), indent=2, ensure_ascii=False))
    # print(json.dumps(get_company_info('839499'), indent=2, ensure_ascii=False))

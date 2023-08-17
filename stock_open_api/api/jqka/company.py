# -*- coding: utf-8 -*-
"""
@File    : company.py
@Date    : 2023-07-25

同花顺 数据接口
"""
from parsel import Selector

from stock_open_api.utils import request_util, json_util


def get_company_info(code):
    """
    同花顺 股票 详细情况 和 发行相关

    eg:

    查看页面：

    - 个股 http://stockpage.10jqka.com.cn/300763/company
    - 港股 http://stockpage.10jqka.com.cn/HK0700/company/
    - 美股 http://stockpage.10jqka.com.cn/TME/company/

    实际数据页面：http://basic.10jqka.com.cn/300763/company.html

    :param code: 股票代码 eg: 300763
    :type code: str

    :return:
    :rtype: dict

    >>> get_company_info('300763')

    {
      "股票名称": "锦浪科技",
      "股票代码": "300763",
      "详细链接": "http://basic.10jqka.com.cn/300763/company.html",
      "公司名称": "锦浪科技股份有限公司",
      "所属地域": "浙江省",
      "英文名称": "Ginlong Technologies Co.,Ltd.",
      "所属申万行业": "电力设备 — 光伏设备",
      "曾用名": "-",
      "公司网址": "www.ginlong.com",
      "主营业务": "组串式逆变器研发、生产、销售和服务。",
      "产品名称": "",
      "控股股东": "王一鸣",
      "实际控制人": "王一鸣、王峻适、林伊蓓",
      "最终控制人": "王一鸣、王峻适、林伊蓓",
      "董事长": "王一鸣",
      "董秘": "张婵",
      "法人代表": "王一鸣",
      "总经理": "王一鸣",
      "注册资金": "3.97亿元",
      "员工人数": "3994",
      "电话": "86-0574-65802608",
      "传真": "86-0574-65781606",
      "邮编": "315712",
      "办公地址": "浙江省宁波市象山县经济开发区滨海工业园金开路188号",
      "公司简介": "锦浪科技股份有限公司主要从事组串式逆变器研发、生产、销售和服务。公司的主要产品为组串式逆变器,是太阳能光伏发电系统不可缺少的核心设备。公司自2011年起被持续认定为国家高新技术企业。公司是国内较早同时通过欧盟CE认证、澳大利亚SAA认证、美国ETL认证等主流市场认证的组串式并网逆变器生产企业。",
      "成立日期": "2005-09-09",
      "发行数量": "2000.00万股",
      "发行价格": "26.64元",
      "上市日期": "2019-03-19",
      "发行市盈率": "19.6800倍",
      "预计募资": "4.73亿元",
      "首日开盘价": "31.97元",
      "发行": "中签率",
      "实际募资": "5.33亿元",
      "主承销商": "海通证券股份有限公司",
      "历史沿革": "查看全部▼"
    }
    """

    base_url = "http://basic.10jqka.com.cn/{code}/company.html"
    url = base_url.format(code=code)

    res = request_util.get(url)
    res.encoding = res.apparent_encoding

    sel = Selector(text=res.text)
    detail_tds = sel.css("#detail table td")
    publish_tds = sel.css("#publish table td")

    stock_name = sel.css("#stockName::attr(value)").extract_first("")
    stock_code = sel.css("#stockCode::attr(value)").extract_first("")

    item = {
        "股票名称": stock_name,
        "股票代码": stock_code,
        "详细链接": url
    }

    for td in detail_tds + publish_tds:
        key = td.css("strong::text").extract_first("").strip()
        value = td.css("span::text").extract_first("").strip()

        if not value:
            value = td.css("a::text").extract_first("").strip()
        if not value:
            value = td.css("p::text").extract_first("").strip()

        key = key.replace("：", "")
        key = key.replace(" ", "")  # 半角空格(英文符号)\u0020
        key = key.replace("　", "")  # 全角空格(中文符号)\u3000

        if key:
            item[key] = value

    return item


if __name__ == '__main__':
    json_util.dump_json(get_company_info('300763'))

# -*- coding: utf-8 -*-
"""
sh_stock.py
上海证券交易所
"""
import json
import re
import time

from stock_open_api.api.sse import sh_stock_config
from stock_open_api.log import logger
from stock_open_api.utils import request_util


def get_company_info(stock_code):
    """
    股票概况 / 公司信息 / 公司概况

    页面地址
        eg: http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001

    :param stock_code: eg 688001
    :type stock_code: str

    :return:
    :rtype: dict

    >>> get_company_info('688001')
    {
      "公司代码": "688001",
      "上市日-A": "",
      "代码-A": "688001",
      "简称-A": "华兴源创",
      "代码-B": "-",
      "上市日-B": "",
      "可转债简称": "华兴转债",
      "可转债代码": "",
      "可转债转股简称": "华兴转债",
      "可转债转股代码": "118003",
      "公司简称-中": "华兴源创",
      "公司简称-英": "HYC",
      "公司全称-中": "苏州华兴源创科技股份有限公司",
      "公司全称-英": "Suzhou HYC Technology CO., LTD",
      "扩位证券简称": "苏州华兴源创科技",
      "上市时是否盈利": "1",
      "是否具有表决权差异安排": "0",
      "注册地址": "苏州工业园区青丘巷8号",
      "通讯地址": "苏州工业园区青丘巷8号",
      "邮编": "215000",
      "法定代表人": "陈文源",
      "董事会秘书姓名": "",
      "E-mail": "dongmiban@hyc.cn",
      "联系电话": "",
      "网址": "http://www.hyc.cn",
      "CSRC行业": "高端装备",
      "SSE行业": "工业",
      "所属省/直辖市": "江苏",
      "状态-A": "上市",
      "状态-B": "-",
      "是否上证180样本股": "-",
      "是否境外上市": "-",
      "境外上市地": "-"
    }

    """
    url = "http://query.sse.com.cn/commonQuery.do"
    detail_url = f'http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE={stock_code}'
    # print()

    logger.debug('Referer: %s', detail_url)

    params = {
        'jsonCallBack': 'jsonpCallback22015',
        'isPagination': 'false',
        'sqlId': 'COMMON_SSE_ZQPZ_GP_GPLB_C',
        'productid': stock_code,
        '_': int(time.time() * 1000),
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': detail_url,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }

    response = request_util.get(url, params, headers=headers)

    ret = re.match("jsonpCallback22015\((.*)\)", response.text)
    data = json.loads(ret.group(1))['result'][0]

    item = {}
    for key, value in sh_stock_config.company_info_key_map.items():
        item[key] = data.get(value, '').strip()

    return item


if __name__ == '__main__':
    print(json.dumps(get_company_info(688627), indent=2, ensure_ascii=False))

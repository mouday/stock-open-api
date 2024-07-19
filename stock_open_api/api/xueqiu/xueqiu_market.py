# -*- coding: utf-8 -*-
"""
@File    : market.py
@Date    : 2024-07-12
"""
from stock_open_api.api.xueqiu import xueqiu_config, xueqiu_util
from stock_open_api.utils import request_util, convert_util
from parsel import Selector


def get_stock_market(stock_code, english_key=False):
    """
    股票行情

    eg: https://xueqiu.com/S/SH600733
    :param stock_code: SH600733
    :param english_key:
    :return:
    返回值示例
    {
      "最高": "10.24",
      "今开": "9.35",
      "涨停": "10.35",
      "成交量": "628.45万手",
      "最低": "9.28",
      "昨收": "9.41",
      "跌停": "8.47",
      "成交额": "61.77亿",
      "量比": "1.29",
      "换手": "12.96%",
      "市盈率(动)": "亏损",
      "市盈率(TTM)": "亏损",
      "委比": "-63.29%",
      "振幅": "10.20%",
      "市盈率(静)": "亏损",
      "市净率": "10.72",
      "每股收益": "-0.99",
      "股息(TTM)": "--",
      "总股本": "55.74亿",
      "总市值": "567.38亿",
      "每股净资产": "0.95",
      "股息率(TTM)": "--",
      "流通股": "48.48亿",
      "流通值": "493.52亿",
      "52周最高": "10.24",
      "52周最低": "3.56",
      "货币单位": "CNY"
    }
    """
    url = f"https://xueqiu.com/S/{stock_code}"

    r = request_util.get(url)

    sel = Selector(text=r.text)
    stock_name = sel.css('.stock-name::text').extract_first('').strip()
    last_price = sel.css('.stock-info .stock-current strong::text').extract_first('').strip()
    change = sel.css('.stock-info .stock-change::text').extract_first('')
    change_list = change.split(' ')

    change_list = [v.strip() for v in change_list if v and v.strip()]

    print(stock_name)
    stock_info = xueqiu_util.parse_stock_code(stock_name)
    # print(change_list)

    change_rate = ''
    change_value = ''
    if len(change_list) == 2:
        change_value = change_list[0].strip()
        change_rate = change_list[1].strip()

    data = {
        '涨跌额': change_value,
        '涨跌幅': change_rate,
        '最新价': last_price,
        '股票名称': stock_info.get('stock_name'),
        '股票代码': stock_info.get('stock_code'),
    }

    for td in sel.css('.quote-info td'):
        key = td.css('::text').extract_first('').strip('：').strip()
        value = td.css('span::text').extract_first('').strip()
        data[key] = value

    if english_key:
        return convert_util.convert_key(xueqiu_config.MARKET_KEY_MAP, data)
    else:
        return data

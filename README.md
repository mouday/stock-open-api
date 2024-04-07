# Stock Open Api

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stock-open-api)](https://pypi.org/project/stock-open-api)
[![PyPI](https://img.shields.io/pypi/v/stock-open-api.svg)](https://pypi.org/project/stock-open-api)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/stock-open-api?label=pypi%20downloads)](https://pypi.org/project/stock-open-api)
[![Documentation Status](https://readthedocs.org/projects/stock-open-api/badge/?version=latest)](https://stock-open-api.readthedocs.io/zh_CN/latest/?badge=latest)

股票数据接口

数据来自网上公开数据，仅做学习交流使用，不可用于商业用途

- github: [https://github.com/mouday/stock-open-api](https://github.com/mouday/stock-open-api)
- pypi: [https://pypi.org/project/stock-open-api/](https://pypi.org/project/stock-open-api/)
- 项目文档：[https://stock-open-api.readthedocs.io/zh_CN/latest/](https://stock-open-api.readthedocs.io/zh_CN/latest/stock_open_api.html#module-stock_open_api)
- 项目主页：[https://mouday.github.io/stock-open-api/](https://mouday.github.io/stock-open-api/)

## 安装

```bash
pip install stock-open-api

# 或者
pip3 install -U stock-open-api -i https://pypi.org/simple
```

## 使用示例

- 约定：所有接口数据都放在`api` 子包下
- 命名规则：`api/数据源/数据源子分类.方法名`
- 返回数据：字典的键以页面上显示的名称为准

如下获取`上海证券交易所`为数据源的的股票公司概况

```python
# -*- coding: utf-8 -*-

from stock_open_api.api.sse import sh_stock

if __name__ == '__main__':
    print(sh_stock.get_company_info('688001'))
```

返回数据

```json
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
```

## 已实现整合数据

数据源：上海证券交易所 [www.sse.com.cn](http://www.sse.com.cn/)

| 数据 | 方法名 |
| - | - | 
| [公司概况](http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001) | api/sse/sh_stock.get_company_info |

数据源：东方财富 [www.eastmoney.com](https://www.eastmoney.com/)

| 数据 | 方法名 |
| - | - | 
| [港股-列表](http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001) | api/eastmoney/hk_stock.get_list |
| [港股-公司资料](http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile) | api/eastmoney/hk_stock.get_org_profile |
| [港股-证券资料](http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile) | api/eastmoney/hk_stock.get_security_info |
| [中国概念股-列表](http://quote.eastmoney.com/center/gridlist.html#us_chinese) | api/eastmoney/us_chinese_stock.get_list |
| [中国概念股-公司资料](http://emweb.eastmoney.com/PC_USF10/pages/index.html?code=PWM&type=web&color=w#/gsgk/gszl) | api/eastmoney/us_chinese_stock.get_org_profile |
| [中国概念股-证券资料](http://emweb.eastmoney.com/PC_USF10/pages/index.html?code=PWM&type=web&color=w#/gsgk/zqzl) | api/eastmoney/us_chinese_stock.get_security_info |
| [科创板-列表](http://quote.eastmoney.com/center/gridlist.html#kcb_board) | api/eastmoney/kcb_stock.get_list |
| [科创板-基本资料+发行相关](http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801) | api/eastmoney/kcb_stock.get_company_info |
| [新三板-列表](http://quote.eastmoney.com/center/gridlist.html#neeq_stocks) | api/eastmoney/neeq_stock.get_list |
| [新三板-公司资料+证券资料](http://xinsanban.eastmoney.com/F10/CompanyInfo/Introduction/839499.html) | api/eastmoney/neeq_stock.get_company_info |
| [A股-基本资料+发行相关](http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801) | api/eastmoney/company.get_company_info |
| [深圳A股-基本资料+发行相关](http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801) | api/eastmoney/sz_stock.get_company_info |
| [上证A股-基本资料+发行相关](http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801) | api/eastmoney/sh_stock.get_company_info |

数据源：犀牛之星 [https://www.ipo3.com/](https://www.ipo3.com/)

| 数据 | 方法名 |
| - | - | 
| [股票详情](https://www.ipo3.com/company-show/stock_code-430510.html) | api/ipo3/neeq_stock.get_company_info |
| [利润表](https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001.html#content) | api/ipo3/neeq_stock.get_income_statement_list |
| [资产负债表](https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-debt.html#content) | api/ipo3/neeq_stock.get_balance_sheet_list |
| [现金流量表](https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-cash.html#content) | api/ipo3/neeq_stock.get_cash_flows_statement_list |
| [财务分析表](https://www.ipo3.com/company-show/stock_code-430510-tab-finance-date_type-001-type-analysis.html#content) | api/ipo3/neeq_stock.get_financial_analysis_list |


## 升级记录 
 
[CHANGELOG.md](https://github.com/mouday/stock-open-api/blob/master/CHANGELOG.md)

## 其他相关库

- AKShare 开源财经数据接口库 
    - github: [https://github.com/akfamily/akshare](https://github.com/akfamily/akshare)
    - doc: [https://akshare.akfamily.xyz/](https://akshare.akfamily.xyz/)

- Tushare 免费提供各类数据 , 助力行业和量化研究。 
    - github: [https://github.com/waditu/tushare](https://github.com/waditu/tushare)
    - doc: [http://tushare.org/index.html](http://tushare.org/index.html)
    - pro doc: [https://tushare.pro/](https://tushare.pro/)

- OpenAPI 量化接口
    - doc: [https://openapi.futunn.com/futu-api-doc/](https://openapi.futunn.com/futu-api-doc/)
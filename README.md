# Stock Open Api

股票数据接口

数据来自网上公开数据，仅做学习交流使用，不可用于商业用途

- github: [https://github.com/mouday/stock-open-api](https://github.com/mouday/stock-open-api)
- pypi: [https://pypi.org/project/stock-open-api/](https://pypi.org/project/stock-open-api/)

## 安装

```bash
pip install stock-open-api
```

## 使用示例

- 约定：所有接口数据都放在`api` 子包下
- 命名规则：`/api/数据源/子类数据源.获取数据的方法名`

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

数据源：上海证券交易所

| 数据 | 方法名 |
| - | - | 
| [公司概况](http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001) | api/sse/sh_stock.get_company_info |

数据源：东方财富

| 数据 | 方法名 |
| - | - | 
| [港股列表](http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001) | api/eastmoney/hk_stock.get_list |
| [港股列表迭代器](http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=688001) | api/eastmoney/hk_stock.get_list_iter |
| [公司资料](http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile) | api/eastmoney/hk_stock.get_org_profile |
| [证券资料](http://emweb.securities.eastmoney.com/PC_HKF10/pages/home/index.html?code=00491&type=web&color=w#/CompanyProfile) | api/eastmoney/hk_stock.get_security_info |

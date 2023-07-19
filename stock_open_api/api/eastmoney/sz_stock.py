# -*- coding: utf-8 -*-
"""
@File    : sz_stock.py
@Date    : 2023-07-18
深圳证券交易所
"""

from stock_open_api.api.eastmoney import company
from stock_open_api.utils import json_util


def get_company_info(code):
    """
    深圳证券交易所 公司 基本资料 | 发行相关
    http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/Index?type=web&code=sh603801

    :param code: str eg: 688627

    :return:
    :rtype: dict

    >>> get_company_info('688627')
        {
          "公司名称": "志邦家居股份有限公司",
          "英文名称": "Zbom Home Collection Co.,Ltd",
          "A股代码": "603801",
          "A股简称": "志邦家居",
          "A股扩位简称": null,
          "曾用名": "志邦股份",
          "B股代码": null,
          "B股简称": null,
          "H股代码": null,
          "H股简称": null,
          "证券类别": "上交所主板A股",
          "上市交易所": "上海证券交易所",
          "所属东财行业": "轻工制造-家具-家具制造",
          "所属证监会行业": "鲁昌华,张京跃,王文兵",
          "总经理": "许帮顺",
          "法人代表": "孙志勇",
          "董秘": "孙娟",
          "董事长": "孙志勇",
          "证券事务代表": "臧晶晶",
          "独立董事": "鲁昌华,张京跃,王文兵",
          "联系电话": "0551-67186564",
          "电子信箱": "zbom@zbom.com",
          "传真": "0551-65203999",
          "公司网址": "www.zbom.com",
          "办公地址": "安徽省合肥市庐阳工业区连水路19号",
          "注册地址": "安徽省合肥市庐阳工业区连水路19号",
          "区域": "安徽",
          "邮政编码": "230061",
          "注册资本(元)": 43654.7813,
          "工商登记": "91340100772816763N",
          "雇员人数": 5151,
          "管理人员人数": 16,
          "律师事务所": "安徽天禾律师事务所",
          "会计师事务所": "大华会计师事务所(特殊普通合伙)",
          "公司介绍": "志邦家居股份有限公司创立于1998年,是中国厨柜行业的先行者。现在,志邦专注于整家定制家居的研发、设计、生产与销售。从“更懂生活”的品牌理念出发,以整家生活的定制设计和服务为优势,为亿万家庭提供从厨房到全屋的整家解决方案。作为整家定制领域的专业家居品牌,志邦家居为人们提供整体厨房、全屋定制、木门墙板、成品家配为核心的整家一体化设计、制造、交付业务,在全国拥有六大生产基地,引进国外智能化制造设备,整合优质供应链,确保产品从设计、生产、安装到服务的每一个环节都以人为尺度、以生活为核心,为全球家庭创造理想的家居良品。凭借卓越的品质和口碑,志邦家居获得“中国环境标志认证”“FSC国际森林认证”等60余项国内外权威认证,同时成为国内诸多知名地产商的重要战略合作伙伴;志邦家居的产品远销海外,出口至澳洲、北美、东南亚、中东等国家和地区,是丽思卡尔顿、瑰丽酒店等国际五星级酒店优质供应商,在东南亚开设多家品牌专营店,品牌享誉全球。自2009年起,志邦家居与央视等主流媒体达成战略合作,并于2016年强势进驻纽约时代广场。同年签约前世界跳水冠军郭晶晶女士为品牌形象代言人,并先后联手郎平、杜丽等世界冠军和蔡康永、陈小春、罗嘉良、许茹芸、杨烁、孙杨、吴莫愁、王耀庆、钟汉良、张智霖、李晨等众多明星共同为美好生活赋义。2017年6月30日,志邦家居在上交所A股上市,2019年1月,正式签约世界著名音乐人周杰伦先生为品牌全新形象代言人。未来,我们将以专业的整家定制服务,发现和满足人们对生活空间的需求;以前沿的产品设计,引领和启发人们对生活品质的向往;以稳健的成长,为社会的良性发展创造更多真实的价值。志邦家居致力成为中国家居行业的一流企业、全球家居行业的领先企业,为现实现人们对家的美好想象奋力前行。",
          "经营范围": "家具制造;家具零配件生产;家具零配件销售;家具销售;家具安装和维修服务;地板制造;地板销售;门窗制造加工;门窗销售;金属门窗工程施工;楼梯制造;楼梯销售;家居用品制造;家居用品销售;建筑装饰材料销售;木材加工;家用电器研发;家用电器制造;家用电器销售;家用电器零配件销售;家用电器安装服务;家用纺织制成品制造;非电力家用器具制造;非电力家用器具销售;卫生洁具研发;卫生洁具制造;卫生洁具销售;厨具卫具及日用杂品研发;厨具卫具及日用杂品批发;厨具卫具及日用杂品零售;日用品销售;灯具销售;互联网销售(除销售需要许可的商品);五金产品批发;五金产品零售;燃气器具生产;电子产品销售;第一类医疗器械销售;第二类医疗器械销售;普通货物仓储服务(不含危险化学品等需许可审批的项目);装卸搬运;会议及展览服务;供应链管理服务;专业设计服务;工业设计服务;咨询策划服务;住房租赁;非居住房地产租赁;货物进出口。",
          "成立日期": "2005-04-04",
          "上市日期": "2017-06-30",
          "发行市盈率(倍)": 22.92,
          "网上发行日期": "2017-06-20",
          "发行方式": "网上定价发行,网下询价配售,市值申购",
          "每股面值(元)": 1,
          "发行量(股)": 40000000,
          "每股发行价(元)": 23.47,
          "发行费用(元)": 89434000,
          "发行总市值(元)": 938800000,
          "募集资金净额(元)": 849366000,
          "首日开盘价(元)": 33.8,
          "首日收盘价(元)": 33.8,
          "首日换手率": 0.0914,
          "首日最高价(元)": 33.8,
          "网下配售中签率": 0.02743221,
          "定价中签率": 0.03205759
        }

    """
    return company.get_company_info("SZ{}".format(code))


if __name__ == '__main__':
    print(json_util.format_json(get_company_info('301398')))

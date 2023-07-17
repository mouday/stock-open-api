# -*- coding: utf-8 -*-
"""
stock_config.py
上海证券交易所
"""

# 接口数据映射
company_info_key_map = {
    '公司代码': 'COMPANY_CODE',
    '上市日-A': 'LISTINGDATEA',
    '代码-A': 'SECURITY_CODE_A',
    '简称-A': 'SECURITY_ABBR_A',
    '代码-B': 'SECURITY_CODE_B',
    '上市日-B': 'LISTINGADATEB',
    '可转债简称': 'CHANGEABLE_BOND_ABBR',
    '可转债代码': ' CHANGEABLE_BOND_CODE',
    '可转债转股简称': 'OTHER_ABBR',
    '可转债转股代码': 'OTHER_CODE',
    '公司简称-中': 'COMPANY_ABBR',
    '公司简称-英': 'ENGLISH_ABBR',
    '公司全称-中': 'FULLNAME',
    '公司全称-英': 'FULL_NAME_IN_ENGLISH',
    '扩位证券简称': 'SEC_NAME_FULL',
    '上市时是否盈利': 'IF_PROFIT',
    '是否具有表决权差异安排': 'IF_VOTE_DIFFERENCE',
    '注册地址': 'COMPANY_ADDRESS',
    '通讯地址': 'OFFICE_ADDRESS',
    '邮编': 'OFFICE_ZIP',
    '法定代表人': 'LEGAL_REPRESENTATIVE',
    '董事会秘书姓名': 'SECURITY_OF_THE_BOARD_OF_DIRE',
    'E-mail': 'E_MAIL_ADDRESS',
    '联系电话': 'PHONE',
    '网址': 'WWW_ADDRESS',
    'CSRC行业': 'SMALL_CLASS_NAME',
    'SSE行业': 'SSE_CODE_DESC',
    '所属省/直辖市': 'AREA_NAME_DESC',
    '状态-A': 'STATE_CODE_A_DESC',
    '状态-B': 'STATE_CODE_B_DESC',
    '是否上证180样本股': 'SECURITY_30_DESC',
    '是否境外上市': 'FOREIGN_LISTING_DESC',
    '境外上市地': 'FOREIGN_LISTING_ADDRESS',
}

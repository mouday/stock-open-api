# -*- coding: utf-8 -*-
"""
@File    : iterator_util.py
@Date    : 2023-07-19
"""
from stock_open_api.api.eastmoney import us_chinese_stock


def list_iterator(list_function, *args, **kwargs):
    """
    列表迭代器
    :param list_function:
    :return: list[ListItem]
    """
    page = 0

    while True:
        page += 1

        data = list_function(page=page, *args, **kwargs)

        if len(data.items) == 0:
            break

        yield data


if __name__ == '__main__':
    for data in list_iterator(us_chinese_stock.get_list):
        print(data.to_dict())

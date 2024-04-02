# -*- coding: utf-8 -*-
"""
@File    : iterator_util.py
@Date    : 2023-07-19
"""


def list_iterator(list_function, *args, **kwargs):
    """
    列表迭代器
    :param list_function: (page, *args, **kwargs)
    :return: list[ListItem]
    """
    page = 0

    while True:
        page += 1

        data = list_function(page=page, *args, **kwargs)

        if len(data.items) == 0:
            break

        yield data

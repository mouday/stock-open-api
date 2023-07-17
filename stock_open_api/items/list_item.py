# -*- coding: utf-8 -*-
"""
@File    : ListItem.py
@Date    : 2023-07-17
"""


class ListItem(object):
    """
    列表对象
    """
    items = None
    total = 0

    def __init__(self):
        self.items = []

    def to_dict(self):
        return {
            'items': self.items,
            'total': self.total,
        }

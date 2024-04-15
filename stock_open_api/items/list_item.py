# -*- coding: utf-8 -*-
"""
@File    : list_item.py
@Date    : 2023-07-17
"""


class ListItem(object):
    """
    列表对象
    """
    items = None
    total = 0

    # @since v1.0.5
    has_next_page = False
    current_page = 0
    next_page = 0

    def __init__(self):
        self.items = []

    def to_dict(self):
        return {
            'total': self.total,
            'has_next_page': self.has_next_page,
            'current_page': self.current_page,
            'next_page': self.next_page,
            'items': self.items,
        }

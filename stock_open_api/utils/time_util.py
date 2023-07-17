# -*- coding: utf-8 -*-
"""
@File    : time_util.py
@Date    : 2023-07-17
"""

import time


def get_timespan_13():
    """
    获取13位时间戳
    :return:
    """
    return int(time.time() * 1000)


if __name__ == '__main__':
    print(get_timespan_13())

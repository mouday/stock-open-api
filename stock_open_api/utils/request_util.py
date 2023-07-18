# -*- coding: utf-8 -*-
"""
@File    : request_util.py
@Date    : 2023-07-18

a requests wrapper
"""

import requests

from stock_open_api.utils import ua_util

default_headers = {
    'User-Agent': ua_util.User_Agent
}


def request(method, url, **kwargs):
    kwargs.setdefault('headers', default_headers)
    return requests.request(method, url, **kwargs)


def get(url, params=None, **kwargs):
    return request("get", url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return request("post", url, data=data, json=json, **kwargs)

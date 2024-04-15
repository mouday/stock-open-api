# -*- coding: utf-8 -*-
"""
@File    : url_util.py
@Date    : 2024-04-15
see: https://six.readthedocs.io/
"""

from six.moves import urllib


def url_join(base, url):
    return urllib.parse.urljoin(base, url)

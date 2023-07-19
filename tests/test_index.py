# -*- coding: utf-8 -*-
"""
@File    : test_index.py
@Date    : 2023-07-19
"""
import pytest

from stock_open_api.version import VERSION


def test_version():
    print('VERSION:', VERSION)


if __name__ == '__main__':
    # Shortcut for --capture=no
    pytest.main(["-s", "test_index.py"])

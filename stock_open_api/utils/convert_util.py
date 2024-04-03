# -*- coding: utf-8 -*-
"""
@File    : convert_util.py
@Date    : 2024-04-03
"""


def convert_key(convert_key_map, convert_data):
    """
    中文键和英文键转换
    :param convert_key_map: dict
    :param convert_data: dict
    :return: dict
    """
    def convert(key_map, data):
        if not data:
            return data

        item = {}

        for k, v in key_map.items():

            # 更丰富的配置
            if isinstance(v, dict):
                item_key = v['value']
                children = v.get('children')
                child = v.get('child')

                if child:
                    # dict
                    item_value = convert(child, data.get(k))

                elif children:
                    # list
                    lst = []
                    for child_d in data.get(k):
                        lst.append(convert(children, child_d))

                    item_value = lst
                else:
                    # string
                    item_value = data.get(k, '')
            else:
                item_key = v
                item_value = data.get(k, '')

            item[item_key] = item_value

        return item

    return convert(convert_key_map, convert_data)

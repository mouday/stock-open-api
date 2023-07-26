# -*- coding: utf-8 -*-
"""
@File    : excel_util.py
@Date    : 2023-07-25
"""

from openpyxl.reader.excel import load_workbook



def read_excel(filename):
    book = load_workbook(filename)
    worksheet = book.worksheets[0]

    row_num = 0
    titles = []
    lst = []

    for row in worksheet.rows:
        row_num += 1

        if row_num == 1:
            # 表头
            for cell in row:
                # 移除空格
                value = cell.value.replace(' ', '')
                titles.append(value)
        else:
            # 内容
            item = {}
            for key, cell in zip(titles, row):
                item[key] = cell.value

            lst.append(item)

    return lst

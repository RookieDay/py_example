#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1
# @Author  : RookieDay
# @Site    : 
# @File    : txt_to_xls
# @Software: PyCharm Community Edition
import os,json,xlwt

from collections import OrderedDict

# txt_path = os.path.join(os.path.dirname(__file__),'student.txt')
txt_path = os.path.join(os.path.dirname(__file__),'numbers.txt')


def read_file(txt_path):
    with open(txt_path,encoding='utf-8-sig') as f:
        txt_content = f.read()
    return txt_content

def parse_content(content):
    # https: // docs.python.org / 3.6 / library / json.html 使用object_paris_hook 保证数据顺序不变
    data = json.loads(content,object_pairs_hook=OrderedDict)
    xls_book = xlwt.Workbook() #创建一个工作簿
    xls_sheet = xls_book.add_sheet('Student') #创建一个sheet

    # 方法1 dict转化为list, list是存放的是dict 的key
    # 在遍历它的value
    print(list(data))
    for index, key in enumerate(list(data)):
        xls_sheet.write(index,0,key)
        if type(data[key]) == list:
            for col, j in enumerate(data[key]):
                xls_sheet.write(index,col+1,j)
        else:
            xls_sheet.write(index,1,data[key])
    # 直接遍历dict
    # row = 0
    # for index, lst_value in data.items():
    #     print(index,lst_value)
    #     xls_sheet.write(row,0,index)
    #     if type(lst_value) == list:
    #         column = 1
    #         for item in lst_value:
    #             xls_sheet.write(row,column,item)
    #             column += 1
    #     else:
    #         xls_sheet.write(row,1,lst_value)
    #     row += 1
    #
    #
    xls_book.save('student.xls')


if __name__ == '__main__':
    content = read_file(txt_path)
    parse_content(content)
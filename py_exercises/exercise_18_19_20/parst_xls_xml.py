#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/2
# @Author  : RookieDay
# @Site    : 
# @File    : parst_xls_xml
# @Software: PyCharm Community Edition
import os
import xlrd
from xml.dom.minidom import Document

# xls_path = os.path.join(os.path.dirname(__file__),'student.xls')
# xls_path = os.path.join(os.path.dirname(__file__),'city.xls')
xls_path = os.path.join(os.path.dirname(__file__),'numbers.xls')

def get_xls_content(xls_path,xls_name):
    xls_open = xlrd.open_workbook(xls_name+'.xls')
    xls_sheet = xls_open.sheet_by_name(xls_name)
    # xls_sheet  = xls_open.sheet_by_index(0) # 获取第一个sheet
    print(xls_sheet.nrows)

    xls_data = {}
    # for exercise 18 19
    # for i in range(xls_sheet.nrows):
    #     xls_data[i+1] = xls_sheet.row_values(i)[1:]
    # return xls_data

    # for exercise 18
    # for i in range(xls_sheet.nrows):
    #     xls_row = xls_sheet.row(i)
    #     col_data = []
    #     for j in range(xls_sheet.ncols):
    #         col_data.append(xls_sheet.cell_value(i,j))
    #     xls_data[i+1] = col_data
    # return xls_data

    # for exercise 20
    xls_data = []
    for i in range(xls_sheet.nrows):
        xls_data.append(xls_sheet.row_values(i))
    return xls_data

def insert_to_xml(xls_data,xls_name):
    xml_out = xls_name + '.xml'
    doc = Document()
    # 创建节点
    root_node = doc.createElement('root')
    child_node = doc.createElement(xls_name)
    # 插入节点
    doc.appendChild(root_node)
    root_node.appendChild(child_node)
    # 创建节点
    # comment_node = doc.createComment('学生信息表	"id" : [名字, 数学, 语文, 英文]')
    # comment_node = doc.createComment('城市信息')
    comment_node = doc.createComment('数字信息')
    child_node.appendChild(comment_node)

    txt_node = doc.createTextNode(str(xls_data))
    child_node.appendChild(txt_node)

    with open(xml_out,'wb') as f:
        f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))


if __name__ == '__main__':
    xls_name = os.path.basename(xls_path).split('.')[0]
    xls_data = get_xls_content(xls_path,xls_name)
    print(xls_data)
    insert_to_xml(xls_data,xls_name)
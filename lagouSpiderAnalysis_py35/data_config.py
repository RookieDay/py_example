#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 19:40
# @Author  : RookieDay
# @Site    : 
# @File    : data_config.py
# @Software: PyCharm Community Edition

# 设置全局参数 所要爬取的岗位、城市、区、保存文件
SPIDER_CONFIG = {
    'position': '数据分析',
    'city': '',
    'district': '',
    'output_file' : 'lagou_analysis.csv',
    'rowTitle': ['companyFullName','city','district','positionName',
                 'workYear','jobNature', 'salary','eduction','companySize',
                 'financeStage','industryField','positionAdvantage',
                 'positionLables','industryLables','companyLableList','jobDetail'
                ]
}
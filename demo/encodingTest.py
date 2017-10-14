#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 23:33
# @Author  : RookieDay
# @Site    : 
# @File    : encodingTest.py
# @Software: PyCharm Community Edition

#! /usr/bin/env python
# -*- coding: utf-8 -*-
s = '中文'  # 注意这里的 str 是 str 类型的，而不是 unicode
s.decode('utf-8').encode('gb18030')


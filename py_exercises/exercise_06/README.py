#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Software: PyCharm Community Edition
import os

test_path = './README.py'
print(os.path.basename(test_path))
print(os.listdir('.'))
print([i for i in os.listdir('.') if os.path.isdir(i)])
print([i for i in os.listdir('.') if os.path.isfile(i) and os.path.splitext(i)[1]=='.py'])
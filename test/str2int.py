#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:04
# @Author  : RookieDay
# @Site    : 
# @File    : str2int.py
# @Software: PyCharm Community Edition
from functools import reduce

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, [1])

print(str2int('12'))
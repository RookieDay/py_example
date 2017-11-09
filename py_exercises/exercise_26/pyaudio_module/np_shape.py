#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : np_shape
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import numpy as np

c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c)
print(c.shape)

c.shape = 4,3
print(c)
print(c.shape)

# 当某数轴的参数为 - 1时，根据元素个数，主动盘算此轴的最大长度，入将c数组改成2行
c.shape = 2, -1
print(c)
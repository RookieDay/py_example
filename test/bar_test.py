#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1
# @Author  : RookieDay
# @Site    : 
# @File    : bar_test
# @Software: PyCharm Community Edition
import matplotlib.pyplot as plt
import numpy as np

data = [5, 20, 15, 25, 10]
n = 5
Y1 = np.random.uniform(0,1.0,n)
print(Y1)
plt.bar(range(len(data)), data, fc='g')
plt.show()



print(int('123'))
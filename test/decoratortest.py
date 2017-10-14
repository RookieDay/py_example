#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:14
# @Author  : RookieDay
# @Site    : 
# @File    : decoratortest.py
# @Software: PyCharm Community Edition
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s, %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now(a,b):
    print('2013-03-02',a,b)

# now = log('execute')(now)
now('ana','test')
print(now.__name__)
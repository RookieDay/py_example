#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:34
# @Author  : RookieDay
# @Site    : 
# @File    : typetest.py
# @Software: PyCharm Community Edition


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass

print(type(fn) == types.FunctionType)

# isinstance()就可以告诉我们，一个对象是否是某种类型
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)

# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法
len('ABC')
'ABC'.__len__()

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('ABC'))

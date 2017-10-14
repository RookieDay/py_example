#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:54
# @Author  : RookieDay
# @Site    : 
# @File    : specialtest.py
# @Software: PyCharm Community Edition

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Student('ana'))

# 接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的




# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a, b = b, a+b
            return L

for n in Fib():
    print(n)

f = Fib()
print(f[:5])


# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
class Cat(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='sex':
            return lambda :'lady'
        raise AttributeError('\'Cat\' object has no attribute \'%s\'' % attr)

s = Cat()
s.sex()


# 直接在实例本身上调用 定义一个__call__()方法，就可以直接对实例进行调用
class Map(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

m = Map()
m()

# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# >>> callable(Student())
# True
# >>> callable(max)
# True
# >>> callable([1, 2, 3])
# False
# >>> callable(None)
# False
# >>> callable('str')
# False
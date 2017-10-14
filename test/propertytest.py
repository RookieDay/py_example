#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:44
# @Author  : RookieDay
# @Site    : 
# @File    : propertytest.py
# @Software: PyCharm Community Edition


# 只允许对Student实例添加name和age属性
# __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 #实际转化为s.set_score(60)
print(s.score) #实际转化为s.get_score()
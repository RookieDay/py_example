#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:23
# @Author  : RookieDay
# @Site    : 
# @File    : objtest.py
# @Software: PyCharm Community Edition

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

stu = Student('ana',12)
print(stu.get_name())

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
# stu.__name
stu._Student__name
stu.__name = "pp"
print(stu.__name)

# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给stu新增了一个__name变量。
print(stu.get_name())

# 果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

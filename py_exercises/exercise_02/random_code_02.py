#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 20:00
# @Author  : RookieDay
# @Site    : 
# @File    : random_code_02.py
# @Software: PyCharm Community Edition
import uuid,random

def generate_random(code_num=5):
    for j in range(code_num):
        yield uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))

if __name__ == '__main__':
    for i in generate_random(5):
        print(i)

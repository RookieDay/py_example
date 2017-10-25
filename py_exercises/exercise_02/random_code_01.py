#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 19:25
# @Author  : RookieDay
# @Site    : 
# @File    : random_code.py
# @Software: PyCharm Community Edition
# 方法1 使用随机字符串
import random, string

# 获取所有英文字母+数字
all_field = string.ascii_letters + string.digits

# random.sample 获取指定长度片段
def get_random_code():
    return ''.join(random.sample(all_field,5))

# 个数+单节长度
def generate_random(code_num, code_length = 1):
    for j in range(code_num):
        yield '-'.join([get_random_code() for i in range(code_length)])

if __name__ == '__main__':
    for i in generate_random(5,4):
        print(i)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 15:18
# @Author  : RookieDay
# @Site    : 
# @File    : redis_random_code.py
# @Software: PyCharm Community Edition
import uuid, redis


def generate_random(code_num=5):
    for i in range(code_num):
        yield uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))

if __name__ == '__main__':
    r = redis.Redis(host='localhost',port=6379,db=0)
    for i in generate_random(400):
    # 向集合添加一个或多个成员
        r.sadd('code',i)

    # 返回集合中的所有成员
    print(r.smembers('code'))
    # 获取集合的成员数
    print(r.scard('code'))


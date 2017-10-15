#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 14:20
# @Author  : RookieDay
# @Site    : 
# @File    : asynciotest.py
# @Software: PyCharm Community Edition

import asyncio

@asyncio.coroutine
def hello():
    print('hello word')
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print('hello again')
# 获取EventLoop:
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
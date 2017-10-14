#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 23:33
# @Author  : RookieDay
# @Site    : 
# @File    : encodingTest.py
# @Software: PyCharm Community Edition

#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/crazyhacking/article/details/39375535
# http://www.cnblogs.com/guosq/p/6378639.html
# https://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script
# https://blog.ernest.me/post/python-setdefaultencoding-unicode-bytes
# Python 会自动的先将 s 解码为 unicode ，然后再编码成 gb18030。因为解码是python自动进行的，我们没有指明解码方式，python 就会使用 sys.defaultencoding 指明的方式来解码。很多情况下 sys.defaultencoding 是
# ANSCII，如果 s 不是这个类型就会出错。拿上面的情况来说，我的 sys.defaultencoding 是 anscii，而 s 的编码方式和文件的编码方式一致，是 utf8 的，所以出错了:
s = '中文'  # 注意这里的 str 是 str 类型的，而不是 unicode
s.decode('utf-8').encode('gb18030')
s.decode('ascii')
u'ANSCII'.encode('UTF-8')


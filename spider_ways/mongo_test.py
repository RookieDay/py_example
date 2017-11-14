#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14
# @Author  : RookieDay
# @Site    : 
# @File    : mongo_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.ana_news
print(db)
for item in db.ana_coll.find():
    print(item)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14
# @Author  : RookieDay
# @Site    : 
# @File    : multi_spider
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from multiprocessing import Pool
from pymongo import MongoClient
import re
import datetime
import json
import requests

host = 'localhost'
port = 27017
name = ''
password = ''
data_base = 'ana_news'
colls = 'ana_coll'
source = "wallstreetcn"

class MongoDBIO:
    def __init__(self,host,port,name,password,database,collection):
        self.host = host
        self.port = port
        self.name = name
        self.password = password
        self.database = database
        self.collection = collection

    def connection_db(self):
        conn = MongoClient(self.host, self.port)
        db = conn[self.database]
        print(db)
        if self.name or self.password:
            # 验证用户名密码
            db.authenticate(name=self.name,password=self.password)
        posts = db[self.collection]
        return posts

def Spider_ur(url,data):
    return requests.get(url=url,params=data).text

def data_process_db(data):
    createdtime = datetime.datetime.now()
    coll = MongoDBIO(host,port,name,password,data_base,colls).connection_db()
    page = (data['paginator'] if 'paginator' in data and data['paginator'] else ' ')
    results = data['results']

    for index,data in enumerate(results):
        db_process = {
            'id':(data['id'] if 'id' in data and data['id'] else ' '),
            'page':(data['id'] if 'id' in data and data['id'] else ' '),
            'type':(data['type'] if 'type' in data and data['type'] else ' '),
            'title':(data['title'] if 'title' in data and data['title'] else ' '),
            'source':source,
            'userId':(data['userId'] if 'userId' in data and data['userId'] else ' '),
            'createdtime':createdtime
        }
        coll.save(db_process)

def func_process(page):
    url = "http://api.wallstreetcn.com/v2/livenews"
    data = {
        'page':page
    }
    content = Spider_ur(url,data)
    data = json.loads(content)
    # print(data)
    data_process_db(data)

if __name__ == '__main__':

    pages = [i for i in range(1,3300)]
    pool = Pool(4)
    # pages = [i for i in range(1, 3)]
    pool.map_async(func_process,pages)
    pool.close()
    pool.join()
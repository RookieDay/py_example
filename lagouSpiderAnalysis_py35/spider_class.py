#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 21:38
# @Author  : RookieDay
# @Site    : 
# @File    : SpiderLaGou.py
# @Software: PyCharm Community Edition

import csv,urllib.parse,urllib.request

class SpiderLaGou(object):
    def __init__(self, position, city, district):
        self.px = 'default'
        self.position = position
        self.city = city
        self.district = district

    def write_line(self, output_file, row_title,model):
        with open(output_file, model, newline='') as csvFile:
            # csvFile.write(codecs.BOM_UTF8)     # 防止乱码
            writer = csv.writer(csvFile)
            print('aa--', row_title)
            writer.writerow(row_title)   #写入一行

    def spider_data(self, url, headers, formdata_pram):
        data = urllib.parse.urlencode(formdata_pram).encode("utf-8")
        req = urllib.request.Request(url,data = data,headers = headers )
        res = urllib.request.urlopen(req)
        res_data = res.read()
        return res_data

    def spider_Getdata(self, url, headers):
        print(url)
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        res_data = res.read()
        return res_data


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 21:38
# @Author  : RookieDay
# @Site    : 
# @File    : SpiderLaGou.py
# @Software: PyCharm Community Edition

import csv,codecs,urllib,urllib2

class SpiderLaGou(object):
    def __init__(self, position, city, district):
        self.px = 'default'
        self.position = position
        self.city = city
        self.district = district

    def write_line(self, output_file, row_title,model):
        with open(output_file,model) as csvFile:
            csvFile.write(codecs.BOM_UTF8)     # 防止乱码
            writer = csv.writer(csvFile)
            writer.writerow(row_title)   #写入一行

    def spider_data(self, url, headers, formdata_pram):
        data = urllib.urlencode(formdata_pram)
        req = urllib2.Request(url,data = data,headers = headers )
        res = urllib2.urlopen(req)
        res_data = res.read()
        return  res_data

    def spider_Getdata(self, url):
        req = urllib2.Request(url )
        res = urllib2.urlopen(req)
        res_data = res.read()
        return  res_data

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 19:51
# @Author  : RookieDay
# @Site    : 
# @File    : spider_data.py
# @Software: PyCharm Community Edition

import data_config
import csv,codecs,urllib,urllib2


class SpiderLaGou(object):
    def __init__(self, position, city, district):
        self.px = 'default'
        self.position = position
        self.city = city
        self.district = district

    def write_line(self, output_file, row_title):
        with open(output_file,'wb') as csvFile:
            csvFile.write(codecs.BOM_UTF8)     # 防止乱码
            writer = csv.writer(csvFile)
            writer.writerow(row_title)   #写入一行

    def spider_data(self, position_format, city_format, district_format, formdata_pram):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_' + position_format + '?px=' + self.px + '&city=' + city_format + '&district=' + district_format,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/61.0.3163.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        url = ('https://www.lagou.com/jobs/positionAjax.json?px=' + self.px + '&city=' + city_format +
               '&district=' + district_format + '&needAddtionalResult=false&isSchoolJob=0')

        data = urllib.urlencode(formdata_pram)
        req = urllib2.Request(url,data = data,headers = headers )
        res = urllib2.urlopen(req)
        res_data = res.read()

        return  res_data

if __name__ == '__main__':

    position = data_config.SPIDER_CONFIG['position']
    city = data_config.SPIDER_CONFIG['city']
    district = data_config.SPIDER_CONFIG['district']
    output_file = data_config.SPIDER_CONFIG['output_file']
    row_title = data_config.SPIDER_CONFIG['rowTitle']

    spider = SpiderLaGou(position, city, district)
    spider.write_line(output_file, row_title)

    position_format = urllib.quote(spider.position)
    city_format = urllib.quote(spider.city)
    district_format = urllib.quote(spider.district)

    formdata_pram = {
        'first': 'true',
        'pn': 1,
        'kd': spider.position
    }

    res_Data = spider.spider_data(position_format, city_format, district_format, formdata_pram)
    print(res_Data)
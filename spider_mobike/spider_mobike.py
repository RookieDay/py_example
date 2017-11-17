#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17
# @Author  : RookieDay
# @Site    : 
# @File    : spider_mobike
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import time,requests

session = requests.session()

headers = {
    'Host':'mwx.mobike.com',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN',
    'Referer ':'https://servicewechat.com/wx80f809371ae33eda/140/page-frame.html',
    'opensrc':'list',
    'platform':'3',
    'Connection':'keep-alive',
    'citycode':'010',
    'lang':'zh'
}

def spider_data():
    headers['time'] = str((time.time() * 1000))
    param = {
        'verticalAccuracy': 10,
        'speed' : -1,
        'longitude': '116.3103',
        'horizontalAccuracy':65,
        'errMsg':  'getLocation:ok',
        'latitude': '39.98518',
        'accuracy': 65,
        'altitude': '51.64844512939453',
        'citycode':'010',
        'wxcode' : ''
    }
    res = session.post(url='https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do',data=param,headers=headers).json()
    for bike in res['object']:
        print('{distId}\t{distX}\t{distY}\t{distNum}\t{distance}\t{bikeIds}\t{biketype}\t{type}\t{boundary}'.format(**bike))

if __name__ == '__main__':
    spider_data()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15
# @Author  : RookieDay
# @Site    : 
# @File    : proxies_spider
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 代理IP可以使用 http://www.xicidaili.com/
# 务必注意http还是https 以及端口号

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
proxies = {
    "http": "http://113.116.141.11:9797",
    "http": "http://61.155.164.108:3128"
}
url = "https://www.zhihu.com"

html=requests.get(url,headers=headers,timeout=3,proxies=proxies).text
print(html)
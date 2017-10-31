#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31
# @Author  : RookieDay
# @Site    : 
# @File    : spider_img
# @Software: PyCharm Community Edition
import urllib.parse,urllib.request
import bs4,os,random

page_num = 1
base_path = os.path.join(os.path.dirname(__file__),'image_out')
def get_form_data(page_num, num_entries = 2):
    url = 'http://tieba.baidu.com/p/2166231880'
    # get 获取数据
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        res_data = res.read()
    except urllib.error.URLError as e:
        print('Download error:' % e.reason)
        html = None
        if num_entries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return get_form_data(url,num_entries-1)
    return res_data

def parse_content_txt(html_content):
    if html_content:
        soup = bs4.BeautifulSoup(html_content,'lxml')
        # 可以使用两种方式获取img src链接
        # for link in soup.find_all(name='img',attrs={'src':re.compile(r'^http')}):
        for link in soup.find_all(name='img',attrs={'class':'BDE_Image'}):
            print(link.get('src'))
            out_path = base_path + '\\out_image' + str(random.randint(1,1000)) + '.jpg'
            urllib.request.urlretrieve(link.get('src'),out_path)

if __name__ == '__main__':
    html_content = get_form_data(page_num,3)
    parse_content_txt(html_content)
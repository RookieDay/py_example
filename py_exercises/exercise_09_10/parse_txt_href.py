#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30
# @Author  : RookieDay
# @Site    : 
# @File    : parse_txt_href
# @Software: PyCharm Community Edition
import urllib.parse,urllib.request
import bs4, re

page_num = 1
def get_form_data(page_num, num_entries = 2):
    desc = ''
    job_desc_url = 'https://www.lagou.com/jobs/'
    job_desc_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'user_trace_token=20170705100900-217dce3ec3e849f9b9feb657eda58a28; LGUID=20170705100900-e9347cd6-6126-11e7-a2a1-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; SEARCH_ID=6ad249accf6d4cd79ae845ca01e36fdd; JSESSIONID=ABAAABAAAFCAAEGDE15343D59135197A109612877A200A0; _gid=GA1.2.1330881492.1508162762; _ga=GA1.2.916608649.1499220527; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507903568,1507958167,1508063140,1508162762; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508164432; LGRID=20171016223356-0a41c8c7-b27f-11e7-9937-525400f775ce',
        'Host': 'www.lagou.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers = {'User-Agent': user_agent}
    url = job_desc_url + str(3597875) + '.html'
    print(url)
    # get 获取数据
    try:
        req = urllib.request.Request(url, headers=headers)
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
        # extract() 方法将当前tag移除文档树, 并作为方法结果返回:
        # 删除里面的script标签
        [sp.extract() for sp in soup('script')]
        print(' '.join(soup.get_text().split()))
        # print(soup.get_text())
        for link in soup.find_all(name='a',attrs={'href':re.compile(r'^http')}):
            print(link.get('href'))

if __name__ == '__main__':
    html_content = get_form_data(page_num,3)
    parse_content_txt(html_content)
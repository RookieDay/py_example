#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17
# @Author  : RookieDay
# @Site    : 
# @File    : download_PDF
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


# download pdf from http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm
import os
import re
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import urllib.request
# parse url
url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm'
# pdf/py url
down_url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/'
out_path = os.path.join(os.path.dirname(__file__),'PDF_Folders')

# 先存储在下载
def save_data():
    res = requests.get(url)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'html.parser')
    prev_save = {}
    for tr_node in soup.find_all('tr'):
        index_middle = tr_node.find_all('td', align='middle')
        if index_middle and index_middle[0].get_text().strip():
            td_nodes_link = tr_node.find_all('td',align='left')[0]
            td_nodes_text = tr_node.find_all('td',align='left')[1].get_text()
            content_name = td_nodes_link.get_text().split('，')[0]
            links = {}
            urls = []
            for link in td_nodes_link.find_all('a',href = re.compile('(.*).py|pdf$')):
                urls.append((down_url + link['href'],link['href']))
            links['remark'] = td_nodes_text
            links['urls'] = urls
            prev_save[content_name] = links
    return prev_save

def download_PDF(prev_save,pool):
    for bs_dir, data in prev_save.items():
        try:
            os.mkdir(bs_dir)
        except:
            pass
        os.chdir(bs_dir)
        with open('%s.txt' % bs_dir, 'w') as f:
            f.write(str(data['remark']))
            print(str(bs_dir), '...done')
        pool.starmap(urllib.request.urlretrieve, data['urls'])
        os.chdir('..')
    pass

if __name__ == '__main__':
    prev_save = save_data()
    try:
        os.makedirs(out_path)
    except:
        pass
    os.chdir(out_path)
    pool=Pool(4)
    download_PDF(prev_save,pool)


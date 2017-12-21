#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18
# @Author  : RookieDay
# @Site    : 
# @File    : thread_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import time
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    ]


# 单线程
start = time.time()
results = map(urllib.request.urlopen, urls)
print(list(results))
print ('Normal:', time.time() - start)

# 多线程
start2 = time.time()
# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(urllib.request.urlopen, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()
print ('Thread Pool:', time.time() - start2)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 21:49
# @Author  : RookieDay
# @Site    : 
# @File    : parse_res_tools.py
# @Software: PyCharm Community Edition

from bs4 import BeautifulSoup
import json,time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_job_description(positionId,spider):

    desc = ''
    job_desc_url = 'https://www.lagou.com/jobs/'
    job_desc_headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'user_trace_token=20170705100900-217dce3ec3e849f9b9feb657eda58a28; LGUID=20170705100900-e9347cd6-6126-11e7-a2a1-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; SEARCH_ID=b3100bc7baac495fa0442be20485a00f; JSESSIONID=ABAAABAACBHABBICDC3CDA27CF0B2DB24BD6FD4FCED92F2; _gid=GA1.2.2067912266.1507730554; _ga=GA1.2.916608649.1499220527; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506522430,1507636866,1507730553,1507807904; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507816623; LGRID=20171012215718-4297ba4e-af55-11e7-9024-525400f775ce',
        'Host':'www.lagou.com',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    url = job_desc_url + str(positionId) + '.html'
    # python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码
    data_html = spider.spider_Getdata(url).decode('utf-8')
    if data_html:
        soup = BeautifulSoup(data_html,'lxml')
        job_desc = soup.find('dd',{'class':'job_bt'})
        if job_desc:
            desc_details = job_desc.findAll('p')
            for detail in desc_details:
                if detail.string:
                    desc += str(detail.string) + '\t'
    return desc

def parse_resdata(res_data,spider,output_file):
    count = 0
    print(res_data)
    data = json.loads(res_data,object_hook=byteify)
    # data = yaml.safe_load(res_data)
    print(data)
    if data.has_key('content') and data['content'].has_key('positionResult') \
            and data['content']['positionResult'].has_key('result'):
            results = data['content']['positionResult']['result']
            for result in results:

                positionId = (result['positionId'] if 'positionId' in result else '')
                job_detailMsg = get_job_description(positionId,spider)
                count += 1
                companyFullName = (result['companyFullName'] if result.has_key('companyFullName') and result['companyFullName'] else '')
                city = (result['city'] if result.has_key('city') and result['city'] else '')
                district = (result['district'] if result.has_key('district') and result['district'] else '')
                positionName = (result['positionName'] if result.has_key('positionName') and result['positionName'] else '')
                workYear = (result['workYear'] if result.has_key('workYear') and result['workYear'] else '')
                jobNature = (result['jobNature'] if result.has_key('jobNature') and result['jobNature'] else '')
                salary = (result['salary'] if result.has_key('salary') and result['salary'] else '')
                eduction = (result['eduction'] if result.has_key('eduction') and result['eduction'] else '')
                companySize = (result['companySize'] if result.has_key('companySize') and result['companySize'] else '')
                financeStage = (result['financeStage'] if result.has_key('financeStage') and result['financeStage'] else '')
                industryField = (result['industryField'] if result.has_key('industryField') and result['industryField'] else '')
                positionAdvantage = (result['positionAdvantage'] if result.has_key('positionAdvantage') and result['positionAdvantage'] else '')
                positionLables = (','.join(result['positionLables']) if result.has_key('positionLables') and result['positionLables'] else '')
                industryLables = (','.join(result['industryLables']) if result.has_key('industryLables') and result['industryLables'] else '')
                companyLableList = (','.join(result['companyLabelList']) if result.has_key('companyLabelList') and result['companyLabelList'] else '')

            line_data = [companyFullName,city,district,positionName,workYear,jobNature, salary,eduction,companySize,
                 financeStage,industryField,positionAdvantage,positionLables,industryLables,companyLableList,str(job_detailMsg)]

            spider.write_line(output_file,line_data,'ab')
            time.sleep(5)
    return count

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

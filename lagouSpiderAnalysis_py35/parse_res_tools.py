#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 21:49
# @Author  : RookieDay
# @Site    : 
# @File    : parse_res_tools.py
# @Software: PyCharm Community Edition

import bs4
import json,time

def get_job_description(positionId,spider):

    desc = ''
    job_desc_url = 'https://www.lagou.com/jobs/'
    job_desc_headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'user_trace_token=20170705100900-217dce3ec3e849f9b9feb657eda58a28; LGUID=20170705100900-e9347cd6-6126-11e7-a2a1-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; SEARCH_ID=6ad249accf6d4cd79ae845ca01e36fdd; JSESSIONID=ABAAABAAAFCAAEGDE15343D59135197A109612877A200A0; _gid=GA1.2.1330881492.1508162762; _ga=GA1.2.916608649.1499220527; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507903568,1507958167,1508063140,1508162762; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508164432; LGRID=20171016223356-0a41c8c7-b27f-11e7-9937-525400f775ce',
        'Host':'www.lagou.com',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    user_agent= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers = {'User-Agent':user_agent}
    url = job_desc_url + str(positionId) + '.html'
    # python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码
    data_html = spider.spider_Getdata(url,job_desc_headers).decode('utf-8')
    if data_html:
        soup = bs4.BeautifulSoup(data_html, 'lxml')
        job_desc = soup.find('dd',{'class':'job_bt'})
        if job_desc:
            desc_details = job_desc.findAll('p')
            for detail in desc_details:
                if detail.string:
                    desc += str(detail.string) + '\t'
        time.sleep(2)
    print(desc)
    return desc.encode('utf-8')

def parse_resdata(res_data,spider,output_file):
    count = 0
    # 将 JSON 对象转换为 Python 字典
    data = json.loads(res_data)
    if 'content' in data and 'positionResult' in data['content']\
            and 'result' in data['content']['positionResult']:
            results = data['content']['positionResult']['result']
            for result in results:
                positionId = (result['positionId'] if 'positionId' in result else '')
                job_detailMsg = get_job_description(positionId, spider)
                count += 1
                print(count)
                companyFullName = (result['companyFullName'] if 'companyFullName' in result and result['companyFullName'] else '')
                city = (result['city'] if 'city' in result and result['city'] else '')
                district = (result['district'] if 'district' in result and result['district'] else '')
                positionName = (result['positionName'] if 'positionName' in result  and result['positionName'] else '')
                workYear = (result['workYear'] if 'workYear' in result and result['workYear'] else '')
                jobNature = (result['jobNature'] if 'jobNature' in result and result['jobNature'] else '')
                salary = (result['salary'] if 'salary' in result and result['salary'] else '')
                eduction = (result['eduction'] if 'eduction' in result and result['eduction'] else '')
                companySize = (result['companySize'] if 'companySize' in result and result['companySize'] else '')
                financeStage = (result['financeStage'] if 'financeStage' in result and result['financeStage'] else '')
                industryField = (result['industryField'] if 'industryField' in result and result['industryField'] else '')
                positionAdvantage = (result['positionAdvantage'] if 'positionAdvantage' in result and result['positionAdvantage'] else '')
                positionLables = (','.join(result['positionLables']) if 'positionLables' in result and result['positionLables'] else '')
                industryLables = (','.join(result['industryLables']) if 'industryLables' in result and result['industryLables'] else '')
                companyLableList = (','.join(result['companyLabelList']) if 'companyLabelList' in result and result['companyLabelList'] else '')

                line_data = [companyFullName,city,district,positionName,workYear,jobNature, salary,eduction,companySize,
                     financeStage,industryField,positionAdvantage,positionLables,industryLables,companyLableList,str(job_detailMsg)]
                spider.write_line(output_file,line_data,'a+')
    time.sleep(5)
    # print(count)
    return count


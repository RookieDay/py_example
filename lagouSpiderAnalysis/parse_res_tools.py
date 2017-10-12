#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 21:49
# @Author  : RookieDay
# @Site    : 
# @File    : parse_res_tools.py
# @Software: PyCharm Community Edition

import json,time


def parse_resdata(res_data,spider,output_file):

    data = json.loads(res_data)
    if data.has_key('content') and data['content'].has_key('positionResult') \
            and data['content']['positionResult'].has_key('result'):
            results = data['content']['positionResult']['result']
            for result in results:
                print()
                if result.has_key('companyFullName') and result['companyFullName']:
                    companyFullName = result['companyFullName']
                else:
                    companyFullName = ''
                if result.has_key('city') and result['city']:
                    city = result['city']
                else:
                    city = ''
                if result.has_key('district') and result['district']:
                    district = result['district']
                else:
                    district = ''
                if result.has_key('positionName') and result['positionName']:
                    positionName = result['positionName']
                else:
                    positionName = ''
                if result.has_key('workYear') and result['workYear']:
                    workYear = result['workYear']
                else:
                    workYear = ''
                if result.has_key('jobNature') and result['jobNature']:
                    jobNature = result['jobNature']
                else:
                    jobNature = ''
                if result.has_key('salary') and result['salary']:
                    salary = result['salary']
                else:
                    salary = ''
                if result.has_key('eduction') and result['eduction']:
                    eduction = result['eduction']
                else:
                    eduction = ''
                if result.has_key('companySize') and result['companySize']:
                    companySize = result['companySize']
                else:
                    companySize = ''
                if result.has_key('financeStage') and result['financeStage']:
                    financeStage = result['financeStage']
                else:
                    financeStage = ''
                if result.has_key('industryField') and result['industryField']:
                    industryField = result['industryField']
                else:
                    industryField = ''
                if result.has_key('positionAdvantage') and result['positionAdvantage']:
                    positionAdvantage = result['positionAdvantage']
                else:
                    positionAdvantage = ''
                if result.has_key('positionLabels') and result['positionLabels']:
                    positionLabels = ','.join(result['positionLabels'])
                else:
                    positionLabels = ''
                if result.has_key('industryLabels') and result['industryLabels']:
                    industryLabels = ','.join(result['industryLabels'])
                else:
                    industryLabels = ''
                if result.has_key('companyLabelList') and result['companyLabelList']:
                    companyLabelList = ','.join(result['companyLabelList'])
                else:
                    companyLabelList = ''
            print(companyFullName)
            spider.write_line(output_file,'')
            time.sleep(3)

    return ''


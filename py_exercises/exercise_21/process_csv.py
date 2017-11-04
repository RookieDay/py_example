#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/4
# @Author  : RookieDay
# @Site    : 
# @File    : process_csv
# @Software: PyCharm Community Edition
import pandas as pd
import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__),'DataAnalyst.csv')
df = pd.read_csv(file_path,encoding='gb2312')
# 快速预览信息
# print(df.info())

# unique函数可以返回唯一值，数据集中positionId是职位ID，值唯一
print(df.positionId.unique())
print(len(df.positionId.unique()))

# drop_duplicates清洗掉 重复数据
df_duplicated = df.drop_duplicates(subset='positionId',keep='first')
# print(df_duplicated.head(5))
# drop_duplicates函数通过subset参数选择以哪个列为去重基准。keep参数则是保留方式，first是保留第一个，删除后余重复值，last还是删除前面，保留最后一个。duplicated函数功能类似，但它返回的是布尔值。

def cut_word(word,method):
    position = word.find('-')
    length = len(word)
    if position != -1:
        bottomSalary = word[:position-1]
        topSalary = word[position+1:length-1]
    else:
        bottomSalary = word[:word.upper().find('K')]
        topSalary = bottomSalary
    if method == 'bottom':
        return bottomSalary
    else:
        return topSalary

df_duplicated['topSalary'] = df_duplicated.salary.apply(cut_word,method='top')
print(df_duplicated['topSalary'].head(3))
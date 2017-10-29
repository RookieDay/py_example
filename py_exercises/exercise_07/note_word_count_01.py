#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : RookieDay
# @Site    : 
# @File    : note_word_count
# @Software: PyCharm Community Edition
# jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
# sentence 为待提取的文本
# topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
# withWeight 为是否一并返回关键词权重值，默认值为 False
# allowPOS 仅包括指定词性的词，默认值为空，即不筛选
# 关键词提取所使用停止词（Stop Words）文本语料库可以切换成自定义语料库的路径
# 用法： jieba.analyse.set_stop_words(file_name) # file_name为自定义语料库的路径

import os
import jieba
import jieba.analyse
from collections import Counter
import re

re_img = re.compile(r'(.txt)$')
txt_path = './note'
stop_path = './stop_words.txt'
topK = 10

def parse_key_word(note_path):
    with open(note_path,encoding='utf-8') as f:
        txt = f.read()
        jieba.analyse.set_stop_words(stop_path)
        tags = jieba.analyse.extract_tags(txt, topK=topK)
        print(",".join(tags))

def process_all_txt(txt_path):
    for fpath, dirs, files in os.walk(txt_path):
        for file in files:
            note, postfix = os.path.splitext(file)
            if(re_img.match(postfix.lower())):
                note_path = os.path.join(fpath,file)
                # print(note_path)
                parse_key_word(note_path)

if __name__ == '__main__':
    process_all_txt(txt_path)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31
# @Author  : RookieDay
# @Site    : 
# @File    : filtered_words
# @Software: PyCharm Community Edition

import os, re

def check_input(user_input,words_path):
    new_input = ''
    with open(words_path,encoding='utf-8') as f:
        # print('aa', f.readlines())
        # 字符串转列表list出现\ufeff
        word_lists = [word.strip('\n').encode('utf-8').decode('utf-8-sig') for word in f.readlines()]
    print(word_lists)
    for word in word_lists:
        if word in user_input:
            # 多输入的全部内容处理
            new_input = re.sub(word,'*'*len(word),user_input)
            user_input = new_input
    print(new_input)

if __name__ == '__main__':
    user_input = input('Please input:')
    words_path = os.path.join(os.path.dirname(__file__),'filter_words.txt')
    check_input(user_input,words_path)
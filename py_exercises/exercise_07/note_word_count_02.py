#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29
# @Author  : RookieDay
# @Site    : 
# @File    : note_word_count_02
# @Software: PyCharm Community Edition

import os
from collections import Counter
import re

re_img = re.compile(r'(.txt)$')
txt_path = './note'
stop_path = './stop_words.txt'
topK = 10
stop_words=['a','he','an','is','it','are','of','by','the','and','him',
            'for','in','to','was','you','i','his','said','had','that',
            'this','s','t','as','at','she','they','them','their','her',
            'on','but','with','not','in','out','all','so','be','have','were']

def parse_key_word(note_path):
    with open(note_path,encoding='utf-8') as f:
        word_lists = []
        txt = f.read()
        txt, number = re.subn(r'[^a-zA-Z0-9]+', ' ', txt)
        word_lists.extend([word for word in txt.lower().split() if (word not in stop_words)])
        word_dict = Counter(word_lists)
        # print(word_dict.most_common(4))
        print(', '.join([word[0] for word in word_dict.most_common()[:5]]))

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
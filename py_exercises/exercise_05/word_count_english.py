#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 21:45
# @Author  : RookieDay
# @Site    : 
# @File    : word_count.py
# @Software: PyCharm Community Edition

# 统计单词出现次数 并且输出到excel or csv
# 词云图

import matplotlib.pyplot as plt
import numpy
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import csv,re

def read_file(file):
    with open(file) as f:
        txt = f.read()
    return txt

def count_to_txt(content, out_file):
    word_lists = []
    # match = re.findall(r'[^a-zA-Z0-9]+',content)
    # for i in match:
    #     content = content.replace(i, ' ')
    # content = content.replace(r'[^a-zA-Z0-9]+',' ')
    content, number = re.subn(r'[^a-zA-Z0-9]+', ' ' , content)
    word_lists.extend([word for word in content.lower().split()])
    word_dict = dict(Counter(word_lists))
    with open(out_file,'w') as f:
        for k, v in word_dict.items():
            f.write(k + '   ' + str(v) + '\n')

def count_to_csv(content,out_csv):
    word_lists = []
    match = re.findall(r'[^a-zA-Z0-9]+',content)
    for i in match:
        content = content.replace(i, ' ')
    word_lists.extend([word for word in content.lower().split()])
    word_dict = dict(Counter(word_lists))
    with open(out_csv,'w',newline='') as data_csv:
        writer = csv.writer(data_csv)
        writer.writerow(['word','count'])
        for k, v in word_dict.items():
            writer.writerow([k,str(v)])

def render_word(content, src_image):
    img = Image.open(src_image)
    # 获取像素矩阵
    mask = numpy.array(img)
    # adding movie script specific stopwords
    stopwords = set(STOPWORDS)

    wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(content)
    # store default colored image Convert to numpy array.
    default_colors = wc.to_array()
    plt.title("Default colors")
    plt.imshow(default_colors, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wc.to_file(path.join(path.dirname(__file__),'huge_count_english.jpg'))

if __name__ == '__main__':
    txt_file = path.join(path.dirname(__file__),'alice.txt')
    out_file = path.join(path.dirname(__file__),'word_count_english.txt')
    out_csv = path.join(path.dirname(__file__),'word_count_english.csv')
    src_image = path.join(path.dirname(__file__),'huge.jpg')

    # 获取文本文件内容
    print(txt_file)
    content = read_file(txt_file)
    # 写入txt
    count_to_txt(content, out_file)
    # 写入csv
    count_to_csv(content, out_csv)
    render_word(content, src_image)
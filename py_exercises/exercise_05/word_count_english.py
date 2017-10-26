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
import Collections

def read_file(file):
    with open(file) as f:
        txt = f.read()
    return txt

def count_to_file(content):
    word_lists = []
    word_lists.append([word.strip('.?!,()`') for word in content.lower().split()])
    c = Counter()
    word_dict = dict(Counter(word_lists))
    for k, v in word_dict.items():
        print(k, v)

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
    txt_file = path.join(path.dirname(__file__),'ana.txt')
    src_image = path.join(path.dirname(__file__),'huge.jpg')

    # 获取文本文件内容
    content = read_file(txt_file)
    count_to_file(content)
    render_word(content, src_image)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 21:45
# @Author  : RookieDay
# @Site    : 
# @File    : word_count.py
# @Software: PyCharm Community Edition

# 统计单词出现次数 并且输出到excel or csv
# 词云图

# 中文词频统计尚有许多bug 后期修正 未使用jieba.load_userdict(file_name)

import matplotlib.pyplot as plt
import jieba.analyse
import numpy
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
import jieba, csv

def read_file(file):
    with open(file,'rb') as f:
        txt = f.read()
    return txt

def count_to_txt(content, out_file):
    word_dict = dict(Counter(jieba.lcut(content)))
    # print(word_dict)
    with open(out_file,'w',encoding='utf-8') as f:
        for k, v in word_dict.items():
            f.write(k + '   ' + str(v) + '\n')

def count_to_csv(content, out_csv):
    word_lists = []
    print(type(content))
    word_dict = dict(Counter(jieba.lcut(content)))
    print(word_dict)
    with open(out_csv,'w',newline='',encoding='utf_8_sig') as data_csv:
        writer = csv.writer(data_csv)
        writer.writerow(['word','count'])
        for k, v in word_dict.items():
            writer.writerow([k,str(v)])

def txtDict(content):
    result = jieba.analyse.textrank(content, topK=1000, withWeight=True)
    word_dict = dict()
    for i in result:
        word_dict[i[0]] = i[1]
    return word_dict

def render_word(keywords, src_image):
    img = Image.open(src_image)
    # 获取像素矩阵
    graph = numpy.array(img)
    fontPath = 'C:/Windows/Fonts/SIMLI.TTF'
    wc = WordCloud(
        font_path=fontPath,
        background_color='white',
        max_words=1000,
        # 使用的词云模板背景
        mask=graph
    )
    # 基于关键信息生成词云
    wc.generate_from_frequencies(keywords)
    # 读取模板颜色
    img_color = ImageColorGenerator(graph)
    # 生成词云图
    plt.imshow(wc)
    plt.axis('off')
    plt.figure()
    # 用模板图片的颜色覆盖
    plt.imshow(wc.recolor(color_func=img_color))
    # 关闭图像坐标系
    plt.axis('off')
    # 显示
    plt.show()
    wc.to_file(path.join(path.dirname(__file__),'huge_count.jpg'))

if __name__ == '__main__':
    txt_file = path.join(path.dirname(__file__),'shijiuda.txt')
    out_file = path.join(path.dirname(__file__),'word_count_chinese.txt')
    out_csv = path.join(path.dirname(__file__),'word_count_chinese.csv')
    src_image = path.join(path.dirname(__file__),'huge.jpg')

    # 获取文本文件内容
    content = read_file(txt_file)
    # 写入txt
    count_to_txt(content,out_file)
    # 写入csv
    count_to_csv(content,out_csv)
    keywords = txtDict(content)
    render_word(keywords, src_image)
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
import jieba.analyse
import numpy
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


def read_file(file):
    with open(file,'rb') as f:
        txt = f.read()
    return txt

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
    src_image = path.join(path.dirname(__file__),'huge.jpg')

    # 获取文本文件内容
    content = read_file(txt_file)
    keywords = txtDict(content)
    render_word(keywords, src_image)
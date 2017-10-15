#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 15:38
# @Author  : RookieDay
# @Site    : 
# @File    : minEX.py
# @Software: PyCharm Community Edition
# wordcloud 作用如其名。本例核心模块，它把我们带权重的关键词渲染成词云
# matplotlib 绘图模块，主要作用是把wordcloud生成的图片绘制出来并在窗口展示
# numpy 图像处理模块，读取图片生成像素矩阵
# PIL (pip install pillow) 图片处理模块， 打开初始化图片
# jieba 牛逼的分词模块，因为我是从一个txt文本里提取关键词，所以需要 jieba 来分词并统计词频。如果是已经有了现成的数据，不再需要它
import matplotlib.pyplot as plt
import jieba.analyse
import numpy
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

def readTxt(file):
    """
    :param file:
    :return:
    """
    with open(txt_file, 'rb') as f:
        txt = f.read()
    return txt

def textDict(content):
    """
    jieba 提取1000个关键词及其比重
    :param content:
    :return:
    """
    result = jieba.analyse.textrank(content, topK=1000, withWeight=True)
    # 转化为比重字典
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    return keywords

def renderWordCloud(keywords, sourceImg):
    # 获取图片资源
    image = Image.open(sourceImg)
    # 转为像素矩阵
    graph = numpy.array(image)

    # wordcloud 默认字体库不支持中文，这里自己选取中文字体
    fontPath = 'C:/Windows/Fonts/SIMLI.TTF'
    #fontPath = 'C:/Windows/Fonts/mplus-1mn-regular.ttf'
    wc = WordCloud(
        font_path=fontPath,
        background_color='white',
        max_words=1000,
        # 使用的词云模板背景
        mask=graph
    )
    # 基于关键词信息生成词云
    wc.generate_from_frequencies(keywords)
    # 读取模板图片的颜色
    image_color = ImageColorGenerator(graph)
    # 生成词云图
    plt.imshow(wc)
    # 用模板图片的颜色覆盖
    plt.imshow(wc.recolor(color_func=image_color))
    # 关闭图像坐标系
    plt.axis('off')
    # 显示图片--在窗口显示
    plt.show()
    wc.to_file(path.join(path.dirname(__file__), 'out.jpg'))

txt_file = path.join(path.dirname(__file__), 'weicheng.txt')
source_img = path.join(path.dirname(__file__), 'ana.jpg')

content = readTxt(txt_file)
keywords = textDict(content)
renderWordCloud(keywords, source_img)
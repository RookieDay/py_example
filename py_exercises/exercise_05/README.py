#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 21:45
# @Author  : RookieDay
# @Site    : 
# @File    : README.py
# @Software: PyCharm Community Edition

# 词云图官网
# https://amueller.github.io/word_cloud/

# 1.分词
# jieba 分词 https://github.com/fxsjy/jieba
# 主要功能
# 1. jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
# 2. jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
# 3. 待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
# 4. jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
# 5. jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
# 6. jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。
import jieba.analyse
import jieba.posseg as pseg
import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

# 【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
# 【精确模式】: 我/ 来到/ 北京/ 清华大学
# 【新词识别】：他, 来到, 了, 网易, 杭研, 大厦    (此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了)
# 【搜索引擎模式】： 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造

print(jieba.lcut("我来到北京清华大学", cut_all=True))
print(jieba.lcut("我来到北京清华大学"))


# 2. 载入词典
# 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
# 用法： jieba.load_userdict(file_name) # file_name 为文件类对象或自定义词典的路径
# 词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
# 词频省略时使用自动计算的能保证分出该词的词频。

# 3. 调整词典
# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
# 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print(jieba.suggest_freq(('中', '将'), True))
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
print(jieba.suggest_freq('台中', True))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

# 4.基于 TF-IDF 算法的关键词抽取
# import jieba.analyse
# jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
# sentence 为待提取的文本
# topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
# withWeight 为是否一并返回关键词权重值，默认值为 False
# allowPOS 仅包括指定词性的词，默认值为空，即不筛选
# jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件


# 5, 基于 TextRank 算法的关键词抽取
# jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 直接使用，接口相同，注意默认过滤词性。
# jieba.analyse.TextRank() 新建自定义 TextRank 实例
# 基本思想:
# 将待抽取关键词的文本进行分词
# 以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
# 计算图中节点的PageRank，注意是无向带权图
# 词性标注
# jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
# 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
# 用法示例

words = pseg.cut('我爱北京天安门')
for word,flag in words:
    print('%s %s' % (word,flag))


# 并行分词
# 原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升
# 基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows
# 用法：
# jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
# jieba.disable_parallel() # 关闭并行分词模式

# Tokenize：返回词语在原文的起止位置
# 注意，输入参数只接受 unicode
# 默认模式
result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

# 搜索模式
result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
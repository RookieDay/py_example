#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/4
# @Author  : RookieDay
# @Site    : 
# @File    : process_csv
# @Software: PyCharm Community Edition

# 重现 https://zhuanlan.zhihu.com/p/27784143
# 建议使用 jupyter notebook
import pandas as pd
import numpy as np
import os
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file_path = os.path.join(os.path.dirname(__file__),'DataAnalyst.csv')
df = pd.read_csv(file_path,encoding='gb2312')
# 快速预览信息
# print(df.info())

# unique函数可以返回唯一值，数据集中positionId是职位ID，值唯一
print(df.positionId.unique())
print(len(df.positionId.unique()))

# drop_duplicates清洗掉 重复数据
df_duplicates = df.drop_duplicates(subset='positionId',keep='first')
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

df_duplicates['topSalary'] = df_duplicates.salary.apply(cut_word,method='top')
df_duplicates['bottomSalary'] = df_duplicates.salary.apply(cut_word,method='bottom')

# print(df_duplicated['topSalary'].head(3))

# 数据类型转换为数字
df_duplicates.topSalary = df_duplicates.topSalary.astype('int')
df_duplicates.bottomSalary = df_duplicates.bottomSalary.astype('int')

# axis是apply中的参数，axis=1表示将函数用在行，axis=0则是列。
df_duplicates['avgSalary'] = df_duplicates.apply(lambda x:(x.bottomSalary + x.topSalary)/2,axis=1)

# 数据清洗的部分完成。切选出我们想要的内容进行后续分析
df_clean = df_duplicates[['city','companyShortName','companySize',
                          'education','positionName','positionLables',
                          'workYear','avgSalary']]
# print(df_clean.head(2))

# 数据进行几个描述统计
# value_counts是计数，统计所有非零元素的个数，以降序的方式输出Series。
# print(df_clean.city.value_counts())

# 分类数据用value_counts，数值数据用describe，这是最常用的两个统计函数。
# print(df_clean.describe())

# plt.style.use('ggplot')使用R语言中的ggplot2配色作为绘图风格
plt.style.use('ggplot')
# hist函数很方便的就绘制除出直方图
# df_clean.avgSalary.hist()
# 将直方图的宽距继续缩小。
# df_clean.avgSalary.hist(bins=15)
# 观察不同城市、不同学历对薪资的影响。箱线图是最佳的观测方式
# df_clean.boxplot(column='avgSalary',by='city',figsize=(9,7))
def font_change(ax):
    font_zh = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=14) #首先加载字体管理包，设置一个载入中文字体的变量
    for label in ax.get_xticklabels(): #ax.get_xticklabels获取坐标轴刻度，即无法正确显示城市名的白框，利用set_fontpeoperties更改字体。
        label.set_fontproperties(font_zh)
    ax.legend(prop=font_zh)

# 城市对薪资的影响
# ax1 = df_clean.boxplot(column='avgSalary',by='city',figsize=(9,7)) #column选择箱线图的数值，by是选择分类变量，figsize是尺寸
# font_change(ax1)
# 教育对薪资的影响
# ax2 = df_clean.boxplot(column='avgSalary',by='education',figsize=(9,7)) #column选择箱线图的数值，by是选择分类变量，figsize是尺寸
# font_change(ax2)
# 工作年限对工资的影响
# df_clean.sort_values('workYear')
# ax3 = df_clean.boxplot(column='avgSalary',by='workYear',figsize=(9,7)) #column选择箱线图的数值，by是选择分类变量，figsize是尺寸
# font_change(ax3)


# 在by传递多个值，箱线图的刻度自动变成元组，也就达到了横向对比的作用
# 北京和上海这两座城市，学历对薪资的影响
# df_sh_bj = df_clean[df_clean['city'].isin(['上海','北京'])]
# ax4 = df_sh_bj.boxplot(column='avgSalary',by=['education','city'],figsize=(14,6)) #column选择箱线图的数值，by是选择分类变量，figsize是尺寸
# font_change(ax4)

# 同时用到多个维度分析时，可以用groupby函数
# 按city列，针对不同城市进行了分组。不过它并没有返回分组后的结果，只返回了内存地址。这时它只是一个对象，没有进行任何的计算，现在调用groupby的count方法。
cx = df_clean.groupby('city').count()
# 返回的是不同城市的各列计数结果，因为没有NaN，每列结果都是相等的。现在它和value_counts等价。
# print(cx)
# mean方法只针对数值，而各列中只有avgSalary是数值，于是返回了这个唯一结果。
# mn = df_clean.groupby('city').mean()
# print(mn)

# groupby可以传递一组列表，这时得到一组层次化的Series。按城市和学历分组计算了平均薪资
# mn1 = df_clean.groupby(['city','education']).mean()
# print(mn1)

# 调用unstack方法，进行行列转置
# mn2 = df_clean.groupby(['city','education']).mean().unstack()
# print(mn2)

# 换成count，我们在groupby后面加一个avgSalary，说明只统计avgSalary的计数结果，不用混入相同数据
# mn3 = df_clean.groupby(['city','education']).avgSalary.count().unstack()
# print(mn3)

# 不同公司招聘的数据分析师数量，并且计算平均数
# agg函数，同时传入count和mean方法，然后返回了不同公司的计数和平均值两个结果。
# ds1 = df_clean.groupby('companyShortName').avgSalary.agg(['count','mean']).sort_values(by='count',ascending=False)
# print(ds1)

# agg除了系统自带的几个函数，它也支持自定义函数。
# 返回了不同公司中最高薪资和最低薪资的差值。agg是一个很方便的函数，它能针对分组后的列数据进行丰富多彩的计算。
# ds2 = df_clean.groupby('companyShortName').avgSalary.agg(lambda x:max(x)-min(x))
# print(ds2)


# 计算出不同城市，招聘数据分析师需求前5的公司
def topN(df,n=5):
    counts = df.value_counts()
    return counts.sort_values(ascending=False)[:n]

tp1 = df_clean.groupby('city').companyShortName.apply(topN)
print(tp1)
tp2 = df_clean.groupby('city').positionName.apply(topN)
# print(tp2)

# ax1 = df_clean.groupby('city').mean().plot.bar()
# font_change(ax1)

# ax2 = df_clean.groupby(['city','education']).mean().unstack().plot.bar(figsize=(14,6))
# font_change(ax2)


# 将上海和北京的薪资数据以直方图的形式进行对比。因为北京和上海的分析师人数相差较远，所以无法直接对比，需要用normed参数转化为密度。设置alpha透明度，它比箱线图更直观。
# plt.hist(x = df_clean[df_clean.city =="上海"].avgSalary,
#         bins=15,
#         normed=1,
#         facecolor='blue',
#         alpha=0.5)
# plt.hist(x = df_clean[df_clean.city =="北京"].avgSalary,
#         bins=15,
#         normed=1,
#         facecolor='red',
#         alpha=0.5)


# 对数据进行深加工。我们将薪资设立出不同的level
# cut的作用是分桶，它也是数据分析常用的一种方法，将不同数据划分出不同等级，也就是将数值型数据加工成分类数据，在机器学习的特征工程中应用比较多。cut可以等距划分，传入一个数字就好。这里为了更好的区分，我传入了一组列表进行人工划分，加工成相应的标签。
bins = [0,3,5,10,15,20,30,100]
level = ['0-3','3-5','5-10','10-15','15-20','20-30','30-100']
df_clean['level'] = pd.cut(df_clean['avgSalary'],bins=bins,labels=level)
# print(df_clean[['avgSalary','level']])

# 用lambda转换百分比，然后作堆积百分比柱形图(matplotlib好像没有直接调用的函数)。这里可以较为清晰的看到不同等级在不同地区的薪资占比。它比箱线图和直方图的好处在于，通过人工划分，具备业务含义。0～3是实习生的价位，3～6是刚毕业没有基础的新人，整理数据那种，6～10是有一定基础的，以此类推。
# df_level = df_clean.groupby(['city','level']).avgSalary.count().unstack()
# print(df_level)
# df_level_prop = df_level.apply(lambda x:x/x.sum(),axis=1)
# axs = df_level_prop.plot.bar(stacked=True,figsize=(14,6))
# font_change(axs)

#
# print(len(df_clean.positionLables))
# print(type(df_clean.positionLables))
# str方法允许我们针对列中的元素，进行字符串相关的处理，这里的[1:-1]不再是DataFrame和Series的切片，而是对字符串截取，这里把[]都截取掉了。如果漏了str，就变成选取Series第二行至最后一行的数据
# 使用完str后，它返回的仍旧是Series，当我们想要再次用replace去除空格。还是需要添加str的。
# print(df_clean.positionLables.str[1:-1].str.replace(' ',''))

# 通过apply和value_counts函数统计标签数。因为各行元素已经转换成了列表，所以value_counts会逐行计算列表中的标签，apply的灵活性就在于此，它将value_counts应用在行上，最后将结果组成一张新表。
word = df_clean.positionLables.str[1:-1].str.replace(' ','')
df_word = word.dropna().str.split(',').apply(pd.value_counts)
# print(df_word)
# 用unstack完成行列转换，它是统计所有标签在各个职位的出现次数，绝大多数肯定是NaN。
# print(df_word.unstack())

# 将空值删除，并且重置为DataFrame，此时level_0为标签名，level_1为df_index的索引，也可以认为它对应着一个职位，0是该标签在职位中出现的次数，
# print(df_word.unstack().dropna().reset_index())


# groupby计算出标签出现的次数
df_word_counts = df_word.unstack().dropna().reset_index().groupby('level_0').count()
# print(df_word_counts)
# print(df_word_counts.index)
df_word_counts.index = df_word_counts.index.str.replace("'",'')
wordcloud = WordCloud(font_path='C:\\WINDOWS\\Fonts\\simsun.ttc',
                      width=900,height=400,background_color='white')

# 在jupyter中显示图片，所以需要额外的配置figsize，不然wide和height的配置无效
# f, axs = plt.subplots(figsize=(15,15))
wordcloud.fit_words(df_word_counts.level_1)
# axs = plt.imshow(wordcloud)
plt.imshow(wordcloud)
plt.axis('off')
wordcloud.to_file(os.path.join(os.path.dirname(__file__),'ciyun.jpg'))
plt.show()

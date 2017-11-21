# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst,MapCompose,Join

class ZhihuLoginByscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()  # 问题url
    title = scrapy.Field(
        output_processor=Join(),
    ) # 问题标题
    focus = scrapy.Field(
        output_processor=Join(),
    ) # 问题关注者有多少
    read = scrapy.Field(
        output_processor=Join(),
    ) # 问题浏览多少
    description = scrapy.Field(
        output_processor=Join(),
    ) # 问题描述




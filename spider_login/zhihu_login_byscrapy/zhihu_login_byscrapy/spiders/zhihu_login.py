#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20
# @Author  : RookieDay
# @Site    : 
# @File    : zhihu_login
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest
from zhihu_login_byscrapy.items import ZhihuLoginByscrapyItem
import json,time
from PIL import Image
from scrapy.loader import ItemLoader


class ZhihuLoginByscrapy(CrawlSpider):
    name = 'zhihu_scrapy'
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com"
    ]
    rules = (
        Rule(LinkExtractor(allow=('/question/\d+#.*?', )),callback='parse_question',follow=True),
        Rule(LinkExtractor(allow=('/question/\d+', )), callback='parse_question', follow=True),
    )
    headers = {
        'Accept':'* / *',
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
       "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
    }
    def start_requests(self):
        return [Request("https://www.zhihu.com/login/email",headers = self.headers,meta={"cookiejar":1},callback=self.post_login)]

    def post_login(self,response):
        _xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        if _xsrf:
            formdata = {
                '_xsrf': _xsrf,
                'password': '****',
                'remember_me': 'true',
                'email': '*****',
                'captcha': ''
            }
            t = str(int(time.time() * 1000))
            captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
            return [Request(captcha_url, headers=self.headers, meta={"cookiejar": response.meta['cookiejar'], "formdata": formdata},
                            callback=self.parse_captcha)]

    def parse_captcha(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
        # Pillow显示验证码
        img = Image.open('captcha.jpg')
        img.show()
        captcha = input('请需要输入验证码： ')
        formdata = response.meta['formdata']
        formdata['captcha'] = captcha
        return [FormRequest("https://www.zhihu.com/login/email",
                            meta={'cookiejar': response.meta['cookiejar']},
                            method='POST',
                            headers=self.headers,
                            formdata=formdata,
                            callback=self.after_login,
                            dont_filter = True,
                              )]

    def after_login(self,response):
        print('bbb**'*30,response.text)
        for url in self.start_urls:
            yield Request(url, headers=self.headers, meta={'cookiejar': response.meta['cookiejar']}, dont_filter=True)

    def parse_question(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = ItemLoader(item=ZhihuLoginByscrapyItem(), response=response)
        item.add_value('url',response.url)
        item.add_css('title','h1.QuestionHeader-title::text')
        item.add_xpath('read', '(//div[@class="NumberBoard-value"])[1]/text()')
        item.add_xpath('focus', '(//div[@class="NumberBoard-value"])[2]/text()')
        item.add_xpath('description', '//span[@class="RichText CopyrightRichText-richText"]/text()')
        print(item)
        return item.load_item()

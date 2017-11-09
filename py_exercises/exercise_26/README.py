#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# pyaudio 参考
# http://people.csail.mit.edu/hubert/pyaudio/
# 百度语音识别
# https://cloud.baidu.com/product/speech
# 以及查看接口文档
# 需要申请ID
""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'
# 打开浏览器 webbrowser模块

# webbrowser.open(url, new=0, autoraise=True)
# 在系统的默认浏览器中访问url地址，如果new=0,url会在同一个浏览器窗口中打开；如果new=1，新的浏览器窗口会被打开;new=2新的浏览器tab会被打开。
import webbrowser
webbrowser.open('www.baidu.com',new=2,autoraise=True)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 19:22
# @Author  : RookieDay
# @Site    : 
# @File    : img_num.py
# @Software: PyCharm Community Edition
from PIL import Image,ImageDraw,ImageFont
import os

img = Image.open('test.png')
f, e = os.path.splitext('test.png')
# make a blank image for the text, initialized to transparent text color
# Image.new(mode,size,color=None)
txt = Image.new('RGBA',img.size,(255,255,255,0))

# get a font
fnt = ImageFont.truetype('C:/Windows/Fonts/SIMLI.TTF',25)
# get a drawing context draw上下文
d = ImageDraw.Draw(txt)

# draw text, half opacity
# 坐标位置(38,8)  写上汉子，字体为font , 填充色为半透明
d.text((38,8),'中国',font=fnt,fill=(255,255,255,128))

# Image.alpha_composite(im1,im2)
# 将im2复合到im1上，返回一个Image对象
# 参数：im1--第一个图像
#       im2--第二个图像 im1和im2的size要相同。且im1和im2的mode都必须是RGBA
out_img = Image.alpha_composite(img,txt)
out_img.save(f+ '_done.png')


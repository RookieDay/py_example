#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31
# @Author  : RookieDay
# @Site    : 
# @File    : verification_code
# @Software: PyCharm Community Edition
import random, string
from PIL import Image,ImageDraw,ImageFont,ImageFilter


font_path = 'C:/Windows/Fonts/SIMLI.TTF'

def random_str():
    return [random.choice(string.ascii_letters) for _ in range(4)]

def random_color(start = 80,end = 200):
    return (random.randint(start,end), random.randint(start,end), random.randint(start,end))

def generate_code(width = 240, height = 60):
    img = Image.new('RGB',(width,height),(255,255,255))
    # 字体
    fnt = ImageFont.truetype(font_path, 40)
    # 画布对象
    draw = ImageDraw.Draw(img)
    # 像素点颜色填充
    for x in range(0,width):
        for y in range(0,height):
            img.putpixel([x,y],random_color(0,150))
    # 画入随机字符
    strs = random_str()
    for i in range(4):
        draw.text((60*i+20,10),strs[i],font=fnt,fill=random_color())
    # 模糊图像，图像会整体变得模糊
    img.filter(ImageFilter.BLUR)
    # 保存图片
    img.save('random_code.jpg')

if __name__ == '__main__':
    generate_code(240, 60)
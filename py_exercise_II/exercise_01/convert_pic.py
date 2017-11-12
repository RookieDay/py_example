#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12
# @Author  : RookieDay
# @Site    : 
# @File    : convert_pic
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
from PIL import Image
import os

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
png_file = os.path.join(os.path.dirname(__file__),'dd.png')
out_file = os.path.join(os.path.dirname(__file__),'out.txt')
WIDTH = 80
HEIGTH = 80

def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    img = Image.open(png_file)
    img = img.resize((WIDTH,HEIGTH),Image.NEAREST)
    txt = ''
    for i in range(HEIGTH):
        for j in range(WIDTH):
            # im.getpixel:根据坐标取得RGB对应的r，g，b三个值
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'
    print(txt)
    with open(out_file,'w') as f:
        f.write(txt)

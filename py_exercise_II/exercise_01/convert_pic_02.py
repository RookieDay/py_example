#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12
# @Author  : RookieDay
# @Site    : 
# @File    : convert_pic_02
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from PIL import Image
import os

ascii_char = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
count = len(ascii_char)

png_file = os.path.join(os.path.dirname(__file__),'test.png')
out_file = os.path.join(os.path.dirname(__file__),'out_2.txt')
WIDTH = 80
HEIGTH = 80


if __name__ == '__main__':
    img = Image.open(png_file).convert("L")
    img = img.resize((WIDTH,HEIGTH),Image.NEAREST)
    txt = ''
    for i in range(HEIGTH):
        for j in range(WIDTH):
            gray = img.getpixel((j,i))
            print(gray)
            txt += ascii_char[int(((count-1)*gray)/256)]
        txt +='\r\n'
    with open(out_file,'w') as f:
        f.write(txt)

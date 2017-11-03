#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/3
# @Author  : RookieDay
# @Site    : 
# @File    : resize_img_to
# @Software: PyCharm Community Edition
import os,re
from PIL import Image

img_out= os.path.join(os.path.dirname(__file__),'image_out')
re_img = re.compile(r'(.jpg|.png|.jpeg|.bmp)$')

# iPhone6
# iPhone_W = 750
# iPhone_H = 1334

# iPhone6s
iPhone_W = 1080
iPhone_H = 1920


def resize_img(img_path,out_file):
    im = Image.open(img_path)
    w, h = im.size
    if w > iPhone_W:
        w = iPhone_W
        h = iPhone_W*h//w
    if h > iPhone_H:
        h = iPhone_H
        w = iPhone_H*w//h

    img_size = im.resize((w,h),Image.ANTIALIAS)
    img_size.save(out_file)


def process_image(src_path):
    for fpath,dirs,files in os.walk(src_path):
        for file in files:
            img, postfilx = os.path.splitext(file)
            if re_img.match(postfilx.lower()):
                img_path = os.path.join(fpath,file)
                out_file = os.path.join(img_out,'iPhone'+file)
                resize_img(img_path,out_file)

if __name__ == '__main__':
    src_path = os.path.join(os.path.dirname(__file__),'image')
    process_image(src_path)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : RookieDay
# @Site    : 
# @File    : resize_img_02
# @Software: PyCharm Community Edition
# 递归

import os,re
from PIL import Image

iPhone_W = 640
iPhone_H = 1136
imgs = []
out_root = os.path.join(os.path.dirname(__file__),'image_out_02')
re_img = re.compile(r'(.jpg|.png|.jpeg|.bmp)$')

def resize_img(src_path, out_file):
    im = Image.open(src_path)
    w, h = im.size
    print(w, h)
    if w > iPhone_W:
        w = iPhone_W
        h = iPhone_W*h//w
    if h > iPhone_H:
        h = iPhone_H
        w = iPhone_H*w//h

    img_resize = im.resize((w,h),Image.ANTIALIAS)
    img_resize.save(out_file)

def get_img(img_path):
        files = os.listdir(img_path)
        for file in files:
            file_in = os.path.join(img_path,file)
            print(file_in)
            if os.path.isdir(file_in):
                get_img(file_in)
            else:
                img, postfix = os.path.splitext(file_in)
                if (re_img.match(postfix.lower())):
                    out_file = os.path.join(out_root, 'iPhone_' + file)
                    # print(file_in + '===' + out_file)
                    resize_img(file_in, out_file)

get_img('./image')
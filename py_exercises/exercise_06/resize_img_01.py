#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : RookieDay
# @Site    : 
# @File    : resize_img_01
# @Software: PyCharm Community Edition
import os,re
from PIL import Image

iPhone_W = 640
iPhone_H = 1136
out_root = os.path.join(os.path.dirname(__file__),'image_out_01')
re_img = re.compile(r'(.jpg|.png|.jpeg|.bmp)$')

def resize_img(src_path, out_file):
    im = Image.open(src_path)
    w, h = im.size
    if w > iPhone_W:
        w = iPhone_W
        h = iPhone_W*h//w
    if h > iPhone_H:
        h = iPhone_H
        w = iPhone_H*w//h

    img_resize = im.resize((w,h),Image.ANTIALIAS)
    img_resize.save(out_file)

def process_img(src_path):
    for fpath, dirs, files in os.walk(src_path):
        for file in files:
            img, postfix = os.path.splitext(file)
            if(re_img.match(postfix.lower())):
                print(fpath)
                img_path = os.path.join(fpath,file)
                out_file = os.path.join(out_root,'iPhone_' + file)
                resize_img(img_path,out_file)

if __name__ == '__main__':
    src_path = os.path.join(os.path.dirname(__file__),'image')
    process_img(src_path)
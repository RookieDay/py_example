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



def process_image(src_path):
    for 

if __name__ == '__main__':
    src_path = os.path.join(os.path.dirname(__file__),'image')
    process_image(src_path)

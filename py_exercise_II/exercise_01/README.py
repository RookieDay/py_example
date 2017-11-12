#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
# 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
# 我们可以使用灰度值公式将像素的 RGB 值映射到灰度值：
# gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

# by http://pillow.readthedocs.io/en/3.0.x/reference/Image.html?highlight=pixel#PIL.Image.Image.getpixel
# Image.getpixel(xy)
# Returns the pixel value at a given position.
#
# Parameters:	xy – The coordinate, given as (x, y).
# Returns:	The pixel value. If the image is a multi-layer image, this method returns a tuple.

# https://blog.ixxoo.me/argparse.html
# argparse 模块 获取命令行参数

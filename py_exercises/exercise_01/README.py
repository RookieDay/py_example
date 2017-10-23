#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 19:23
# @Author  : RookieDay
# @Site    : 
# @File    : README.py
# @Software: PyCharm Community Edition

# Pillow是Python里的图像处理库（PIL：Python Image Library），提供了了广泛的文件格式支持，强大的图像处理能力，
# 主要包括图像储存、图像显示、格式转换以及基本的图像处理操作等。

# 官网：https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#using-the-image-class
# 导包
from __future__ import print_function
from PIL import Image,ImageFilter
import os,sys
# part1
img = Image.open('test.png')
img_huge = Image.open('huge.jpg')
# format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；
# size属性是一个tuple，表示图像的宽和高（单位为像素）； W, H = img.size
# mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。
print(img.format, img.size, img.mode)
print(img_huge.mode)
# img.show()


# save 保存 转换图片为jpg
img = img.convert('RGB') #图片为RGBA
f1, e = os.path.splitext('test.png')
f1_huge, e_huge = os.path.splitext('huge.jpg')
out_file = f1 + '.jpg'
img.save(out_file)
# save函数的第二个参数可以用来指定图片格式，如果文件名中没有给出一个标准的图像格式，那么第二个参数是必须的。
f2, e = os.path.splitext('test.png')
# img.save(f2,'JPEG')

# 创建缩略图
size = (56,56)
f2_outfile = os.path.splitext('test.png')[0] + ".thumbnail"
img.thumbnail(size)
img.save(f2_outfile,'JPEG')

# 裁剪、粘贴、与合并图片
# crop()方法可以从图片中提取一个子矩形
temp_save = img.copy() #复制图像
box = (0,0,128,128) #(left, upper, right, lower)。 Pillow左边系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点
region = img.crop(box)
region.save(f1 +'_region.png')

# Image类有resize()、rotate()和transpose()、transform()方法进行几何变换。
# 选择45度
img.rotate(45).save(f1 + '_rotete.png')
# 图片左右置换
img.transpose(Image.FLIP_LEFT_RIGHT).save(f1 + '_flip1.png')
# 图片上下置换
img.transpose(Image.FLIP_TOP_BOTTOM).save(f1 + '_flip2.png')
#图片旋转90度
img.transpose(Image.ROTATE_90).save(f1 + '_rotate90.png')

# ImageFilter模块所支持的滤波器
# 模糊图像，图像会整体变得模糊
img_huge.filter(ImageFilter.BLUR).save(f1_huge + '_filter1.jpg')
# 轮廓图像，将图像中的轮廓信息全部提取出来
img_huge.filter(ImageFilter.CONTOUR).save(f1_huge + '_filter2.jpg')
# 细节增强，会使得图像中细节更加明显。
img_huge.filter(ImageFilter.DETAIL).save(f1_huge + '_filter3.jpg')
# 突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法。经处理使得边界和边缘在图像上表现为图像灰度的突变,用以提高人眼识别能力。
img_huge.filter(ImageFilter.EDGE_ENHANCE).save(f1_huge + '_filter4.jpg')

# img_huge.filter(ImageFilter.EDGE_ENHANCE_MORE).save(f1_huge + '_filter5.jpg')
# img_huge.filter(ImageFilter.EMBOSS).save(f1_huge + '_filter6.jpg')
# img_huge.filter(ImageFilter.FIND_EDGES).save(f1_huge + '_filter7.jpg')
# img_huge.filter(ImageFilter.SMOOTH).save(f1_huge + '_filter8.jpg')
# img_huge.filter(ImageFilter.SMOOTH_MORE).save(f1_huge + '_filter9.jpg')
# img_huge.filter(ImageFilter.SHARPEN).save(f1_huge + '_filter10.jpg')

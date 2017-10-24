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
from PIL import Image, ImageFilter, ImageEnhance
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

# part2
# Image类有resize()、rotate()和transpose()、transform()方法进行几何变换。
# 选择45度
img.rotate(45).save(f1 + '_rotete.png')
# 图片左右置换
img.transpose(Image.FLIP_LEFT_RIGHT).save(f1 + '_flip1.png')
# 图片上下置换
img.transpose(Image.FLIP_TOP_BOTTOM).save(f1 + '_flip2.png')
#图片旋转90度
img.transpose(Image.ROTATE_90).save(f1 + '_rotate90.png')

# part3
# ImageFilter模块所支持的滤波器
# 模糊图像，图像会整体变得模糊
img_huge.filter(ImageFilter.BLUR).save(f1_huge + '_filter1.jpg')
# 轮廓图像，将图像中的轮廓信息全部提取出来
img_huge.filter(ImageFilter.CONTOUR).save(f1_huge + '_filter2.jpg')
# 细节增强，会使得图像中细节更加明显。
img_huge.filter(ImageFilter.DETAIL).save(f1_huge + '_filter3.jpg')
# 边缘增强，突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法。经处理使得边界和边缘在图像上表现为图像灰度的突变,用以提高人眼识别能力。
img_huge.filter(ImageFilter.EDGE_ENHANCE).save(f1_huge + '_filter4.jpg')
# 深度边缘增强，会使得图像中边缘部分更加明显
img_huge.filter(ImageFilter.EDGE_ENHANCE_MORE).save(f1_huge + '_filter5.jpg')
# 浮雕，会使图像呈现出浮雕效果
img_huge.filter(ImageFilter.EMBOSS).save(f1_huge + '_filter6.jpg')
# 寻找边缘信息，会找出图像中的边缘信息
img_huge.filter(ImageFilter.FIND_EDGES).save(f1_huge + '_filter7.jpg')
# 平滑，突出图像的宽大区域、低频成分、主干部分或抑制图像噪声和干扰高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量
img_huge.filter(ImageFilter.SMOOTH).save(f1_huge + '_filter8.jpg')
# 深度平滑，会使得图像变得更加平滑
img_huge.filter(ImageFilter.SMOOTH_MORE).save(f1_huge + '_filter9.jpg')
# 锐化，补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
img_huge.filter(ImageFilter.SHARPEN).save(f1_huge + '_filter10.jpg')
# 高斯模糊 >radius指定平滑半径。
img_huge.filter(ImageFilter.GaussianBlur(radius=2)).save(f1_huge + '_filter11.jpg')
# 反锐化掩码 >radius指定模糊半径；>percent指定反锐化强度（百分比）; >threshold控制被锐化的最小亮度变化。
img_huge.filter(ImageFilter.UnsharpMask(radius=12, percent=150, threshold=3)).save(f1_huge + '_filter12.jpg')
# 其他滤波
# • Kernel(size, kernel, scale=None, offset=0)：核滤波
# 当前版本只支持核大小为3x3和5x5的核大小，且图像格式为“L”和“RGB”的图像。
# >size指定核大小（width, height）；
# >kernel指定核权值的序列；
# >scale指定缩放因子；
# >offset指定偏移量，如果使用，则将该值加到缩放后的结果上。
# • RankFilter(size, rank)：排序滤波
# >size指定滤波核的大小；
# >rank指定选取排在第rank位的像素，若大小为0，则为最小值滤波；若大小为size * size / 2则为中值滤波；若大小为size * size - 1则为最大值滤波。
# • MedianFilter(size=3)：中值滤波
# >size指定核的大小
# • MinFilter(size=3)：最小值滤波器
# >size指定核的大小
# • MaxFilter(size=3)：最大值滤波器
# >size指定核的大小
# • ModeFilter(size=3)：波形滤波器
# 选取核内出现频次最高的像素值作为该点像素值，仅出现一次或两次的像素将被忽略，若没有像素出现两次以上，则保留原像素值。
# >size指定核的大小

# part4
# 像素点处理 point()方法通过一个函数或者查询表对图像中的像素点进行处理（例如对比度操作）。
# 像素点变换 且对图片中的每一个点执行这个函数
out_point = img_huge.point(lambda i:i * 1.2 + 10)
out_point.save(f1_huge +'_point.jpg')

# 处理单独通道
out_split = img_huge.split()
print(out_split)
# select regions where red is less than 100
mask = out_split[0].point(lambda i:i < 100 and 255)
# process the green band 像素点*0.7
out_green = out_split[1].point(lambda i:i*0.7)
# paste the processed band back, but only where red was < 100
# im.paste(image,box) box 尺寸复制
# im.paste(image,box, mask)
# 使用变量mask对应的模板图像来填充所对应的区域。可以使用模式为“1”、“L”或者“RGBA”的图像作为模板图像。模板图像的尺寸必须与变量image对应的图像尺寸一致。如果变量mask对应图像的值为255，则模板图像的值直接被拷贝过来；如果变量mask对应图像的值为0，则保持当前图像的原始值。变量mask对应图像的其他值，将对两张图像的值进行透明融合。
# mask 当为0时，保留当前值，255为使用paste进来的值，中间则用于transparency效果
# 注意：如果变量image对应的为“RGBA”图像，即粘贴的图像模式为“RGBA”，则alpha通道被忽略。用户可以使用同样的图像作为原图像和模板图像。
out_split[1].paste(out_green,None,mask)
# build a new multiband image
out_split_jpg = Image.merge(img_huge.mode,out_split)
out_split_jpg.save(f1_huge + '_split.jpg')


# part5
# enhancer.enhance(factor) ⇒ image factor值越小，颜色越少（亮度，对比度等）
# 高级图片增强 对其他高级图片增强，应该使用ImageEnhance模块 。一旦有一个Image对象，应用ImageEnhance对象就能快速地进行设置。 可以使用以下方法调整对比度、亮度、色平衡和锐利度。
# ImageEnhance模块的Color类 从0.1到0.5，再到0.8，2.0，图像的颜色饱和度依次增大
ImageEnhance.Color(img_huge).enhance(0.1).save(f1_huge + '_enchance1.jpg')
ImageEnhance.Color(img_huge).enhance(0.5).save(f1_huge + '_enchance2.jpg')
ImageEnhance.Color(img_huge).enhance(0.8).save(f1_huge + '_enchance3.jpg')
ImageEnhance.Color(img_huge).enhance(2.0).save(f1_huge + '_enchance4.jpg')

# ImageEnhance模块的Brightness类
# 创建一个调整图像亮度的增强对象。增强因子为0.0将产生黑色图像；为1.0将保持原始图像。
# 从0.1到0.5，再到0.8，2.0，图像的亮度依次增大。
ImageEnhance.Brightness(img_huge).enhance(0.1).save(f1_huge + '_brightness1.jpg')
ImageEnhance.Brightness(img_huge).enhance(0.5).save(f1_huge + '_brightness2.jpg')
ImageEnhance.Brightness(img_huge).enhance(0.8).save(f1_huge + '_brightness3.jpg')
ImageEnhance.Brightness(img_huge).enhance(2.0).save(f1_huge + '_brightness4.jpg')

# ImageEnhance模块的Contrast类
# 对比度增强类用于调整图像的对比度。类似于调整彩色电视机的对比度
# 从0.1到0.5，再到0.8，2.0，图像的对比度依次增大。
ImageEnhance.Contrast(img_huge).enhance(0.1).save(f1_huge + '_contrast1.jpg')
ImageEnhance.Contrast(img_huge).enhance(0.5).save(f1_huge + '_contrast1.jpg')
ImageEnhance.Contrast(img_huge).enhance(0.8).save(f1_huge + '_contrast1.jpg')
ImageEnhance.Contrast(img_huge).enhance(2.0).save(f1_huge + '_contrast1.jpg')

# ImageEnhance模块的Sharpness类
# 增强因子为0.0将产生模糊图像；为1.0将保持原始图像，为2.0将产生锐化过的图像。
# 从0.0到2.0，再到3.0，图像的锐度依次增大。
ImageEnhance.Sharpness(img_huge).enhance(0.1).save(f1_huge + '_sharpness1.jpg')
ImageEnhance.Sharpness(img_huge).enhance(0.5).save(f1_huge + '_sharpness2.jpg')
ImageEnhance.Sharpness(img_huge).enhance(0.8).save(f1_huge + '_sharpness3.jpg')
ImageEnhance.Sharpness(img_huge).enhance(2.0).save(f1_huge + '_sharpness4.jpg')


# part6
# 更多读取图片方法
# 从string中读取
# import StringIO
# im = Image.open(StringIO.StringIO(buffer))

# 从tar文件中读取
# from PIL import TarIO
# fp = TarIO.TarIO("Imaging.tar", "Imaging/test/lena.ppm")
# im = Image.open(fp)

# part7
# 草稿模式
# draft()方法允许在不读取文件内容的情况下尽可能（可能不会完全等于给定的参数）地将图片转成给定模式和大小，这在生成缩略图的时候非常有效（速度要求比质量高的场合）。
out_draft = Image.open('huge_brightness4.jpg')
print("original = ", out_draft.mode, out_draft.size)

out_draft.draft("L",(100,100)).save(f1_huge + '_draft.jpg')
print("draft = ", out_draft.mode,out_draft.size)
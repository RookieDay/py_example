#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 19:25
# @Author  : RookieDay
# @Site    : 
# @File    : README.py
# @Software: PyCharm Community Edition

# random 模块 方法1
import random
# 用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.random())

# random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a
print(random.uniform(10,20))
print(random.uniform(20,10))

# random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print(random.randint(12,20))
print(random.randint(21,28))
# print random.randint(20, 10)  #该语句是错误的。下限必须小于上限。

# random.randrange
# random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
# 如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。


# random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
print(random.choice('ana is a daily life'))
print(random.choice(['a','bna','cna']))
print(random.choice(('ana','bna','cna')))


# random.shuffle
# random.shuffle(x[, random])，用于将一个列表中的元素打乱
p = ['ana','bna','cna','and so on']
random.shuffle(p)
print(p)

# random.sample
# random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
print(random.sample([1,2,3,4,5,6,7],5)) # 随机获取5个元素，作为一个片断返回


# uuid 模块 方法2
#     UUID是128位的全局唯一标识符，通常由32字节的字符串表示。
#     它可以保证时间和空间的唯一性，也称为GUID，全称为：
#             UUID —— Universally Unique IDentifier      Python 中叫 UUID
#             GUID —— Globally Unique IDentifier          C#  中叫 GUID
#
#     它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
#     UUID主要有五个算法，也就是五种方法来实现：
#
#        1、uuid1()——基于时间戳
#
#                由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
#                但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
#
#        2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
#
#                 算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
#                 实际中很少用到该方法。
#
#       3、uuid3()——基于名字的MD5散列值
#
#                 通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
#                 和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
#
#        4、uuid4()——基于随机数
#
#                 由伪随机数得到，有一定的重复概率，该概率可以计算出来。
#
#        5、uuid5()——基于名字的SHA-1散列值
#
#                 算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法
# 使用方面：
#
#     首先，Python中没有基于DCE的，所以uuid2可以忽略；
#     其次，uuid4存在概率性重复，由无映射性，最好不用；
#     再次，若在Global的分布式计算环境下，最好用uuid1；
#     最后，若有名字的唯一性要求，最好用uuid3或uuid5。

import uuid

name = 'a'
print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS,name))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS,name))
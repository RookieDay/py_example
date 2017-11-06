#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6
# @Author  : RookieDay
# @Site    : 
# @File    : Hashing Strings with Python
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 翻译自：http://pythoncentral.io/hashing-strings-with-python/

# 哈希函数是接受一个可变长度的字节序列的输入并将其转换为一个固定长度的序列的函数。 这是一个单向函数。
# 这意味着如果f是哈希函数，计算f（x）是相当快速和简单的，但是再次尝试获得x需要几年的时间。 哈希函数返回的值通常称为哈希，
# message digest，哈希值或校验和。 大多数情况下，哈希函数会为给定的输入生成唯一的输出。 然而，根据算法，
# 由于这些函数背后的数学理论，有可能发现冲突。
#
# 现在假设你想用SHA1函数对字符串“Hello Word”进行哈希，结果是0a4d55a8d778e5022fab701977c5d840bbc486d0。
#      input                                            output
# “Hello Word” ---> SHA1('helloword')  ---> 0a4d55a8d778e5022fab701977c5d840bbc486d0
#
#
# 哈希函数用于一些加密算法，数字签名，消息认证码，操纵检测，指纹，校验和（消息完整性检查），散列表，密码存储等等。
# 作为一名Python程序员，您可能需要这些功能来检查重复的数据或文件，在通过网络传输信息时检查数据完整性，在数据库中安全地存储密码，
# 或者可能需要一些与密码相关的工作。
#
# 我想清楚地表明哈希函数不是一个加密协议，它们不加密或解密信息，但它们是许多加密协议和工具的基本组成部分。
#
# 一些最常用的哈希函数是：
# MD5：产生128位散列值的消息摘要算法。这被广泛用于检查数据完整性。由于MD5的安全漏洞，不适用于其他领域。
#
# SHA：由美国国家安全局设计的一组算法，属于美国联邦信息处理标准的一部分。这些算法在很多密码应用中被广泛使用。消息长度从160位到512位。
# Python标准库中包含的hashlib模块是一个包含最流行哈希算法的接口的模块。 hashlib实现了一些算法，但是如果你安装了OpenSSL，hashlib也可以使用这个算法。
#
#
# 这个代码是在Python 3.2及以上版本中工作的。如果你想在Python 2.x中运行这个例子，只需要移除algorithms_available和algorithms_guaranteed调用。
#
# 首先，导入hashlib模块：

import hashlib

# 现在我们使用algorithms_available或algorithms_guaranteed列出可用的算法。

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# algorithms_available方法列出了系统中可用的所有算法，包括可用的OpenSSl算法。 在这种情况下，您可能会在列表中看到重复的名称。
# algorithms_guaranteed只列出模块中存在的算法。 md5，sha1，sha224，sha256，sha384，sha512始终存在。

# MD5
hash_object = hashlib.md5(b'helloword')
print(hash_object.hexdigest())

# 上面的代码使用“Hello World”字符串并打印该字符串的 HEX digest。 十六进制返回一个十六进制表示散列的字符串，
# 以防需要使用摘要的字节序列。

# 注意字符串前面的“b”是很重要的，它将字符串转换为字节，因为哈希函数只将字节序列作为参数。 在以前版本的库中，
# 它使用了字符串文字。 因此，如果您需要从控制台获取一些输入并散列该输入，请不要忘记按字节序列对字符串进行编码：

mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())   #务必字符串转换为字节
print(hash_object.hexdigest())

# SHA1
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA224
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA256
hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA384
hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA512
hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# 使用OpenSSL算法
#
# 现在假设你需要一个由OpenSSL提供的算法。 使用algorithms_available，我们可以找到你想要使用的算法的名称。
# 在这种情况下，我的电脑上可以使用“DSA”。 然后你可以使用new和update的方法：
# hash_object = hashlib.new('DSA')
# hash_object.update(b'Hello World')
# print(hash_object.hexdigest())

# 更多关于安全密码的信息
# https://crackstation.net/hashing-security.htm#attacks
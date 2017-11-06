#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6
# @Author  : RookieDay
# @Site    : 
# @File    : hashing_passwords
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 在下面的例子中，我们将哈希密码存储在数据库中。 在这个例子中，我们使用salt。 salt是在使用哈希函数之前添加到密码字
# 符串的随机序列（意思就是在使用hash函数之前，密码中混入salt）。 盐是用来防止dictionary attacks and rainbow tables attacks。
# 但是，如果您正在制作实际应用程序并使用用户的密码，请务必更新该字段的最新漏洞。 想了解更多关于安全密码的信息，请参
# 考这个 https://crackstation.net/hashing-security.htm

import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')
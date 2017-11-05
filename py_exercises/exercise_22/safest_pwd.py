#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/5
# @Author  : RookieDay
# @Site    : 
# @File    : safest_pwd
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 参考1 http://zhuoqiang.me/password-storage-and-python-example.html

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password,salt=None):
    if salt is None:
        salt = os.urandom(8) #64bits

    assert 8 == len(salt)
    assert isinstance(salt,bytes)
    assert isinstance(password,str)

    if isinstance(password, str):
        password = password.encode('utf-8')
    assert isinstance(password,bytes)

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__ == '__main__':
    hashed = encrypt_password('ana9111')
    assert validate_password(hashed, 'ana9111')

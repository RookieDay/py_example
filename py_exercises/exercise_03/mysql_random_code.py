#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 20:26
# @Author  : RookieDay
# @Site    : 
# @File    : mysql_random_code.py
# @Software: PyCharm Community Edition
from sqlalchemy import Column, String, create_engine, Integer, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

# 创建对象基类
Base = declarative_base()

# 定义USER对象
class Random_code(Base):
    # 表的名字
    __tablename__ = 'random_code'
    # 表的结构
    id = Column(Integer, Sequence('id'),primary_key=True)
    code = Column(String(200))

# 初始化数据库链接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

def generate_random(code_num=5):
    for i in range(code_num):
        yield uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))

if __name__ == '__main__':
    # 关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
    # 向数据库表中添加一行记录，可以视为添加一个User对象
    # 创建session对象
    session = DBSession()
    for i in generate_random(400):
        # 创建新的Random_code对象
        print(i)
        new_code = Random_code(code=str(i))
        # 添加到seesion
        session.add(new_code)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()


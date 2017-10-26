#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 21:49
# @Author  : RookieDay
# @Site    : 
# @File    : create_random.py
# @Software: PyCharm Community Edition

from sqlalchemy import Column, String, create_engine, Integer, Sequence, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test',echo=True)
# 设置metadata并将其绑定到数据库引擎
metadata = MetaData(engine)
Base.metadata.drop_all(engine)
# 定义需新建的表
user_table = Table('random_code', metadata,
        Column('id', Integer,primary_key=True),
        Column('code', String(200))
        )
# 在数据库中创建表
metadata.create_all()
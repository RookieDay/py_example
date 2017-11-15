#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15
# @Author  : RookieDay
# @Site    : 
# @File    : create_mysql_table
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


from sqlalchemy import Column, String, create_engine, Integer, Sequence, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接: ana_db database
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/ana_db',echo=True)
metadata = MetaData(engine)
Base.metadata.drop_all(engine)
user_table = Table('ana_test', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(200))
        )
metadata.create_all()
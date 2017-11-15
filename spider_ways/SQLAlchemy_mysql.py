#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15
# @Author  : RookieDay
# @Site    : 
# @File    : SQLAlchemy_mysql
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from sqlalchemy import Column, String, create_engine, Integer, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import string,random

all_fields = string.ascii_letters + string.digits

# 创建对象基类
Base = declarative_base()

# 定义ana_test对象
class Ana_test(Base):
    # 表的名字
    __tablename__ = 'ana_test'
    # 表的结构
    id = Column(Integer, Sequence('id'),primary_key=True)
    name = Column(String(200))

# 初始化数据库链接 建立数据库引擎
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/ana_db')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

if __name__ == '__main__':
    # 关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
    # 向数据库表中添加一行记录，可以视为添加一个User对象
    # 创建session对象
    session = DBSession()
    str_name = ''.join(random.sample(all_fields,5))
    new_ana = Ana_test(name=str_name)
    # 添加到session:
    session.add(new_ana)
    # 提交即保存到数据库
    session.commit()
    ana_query = session.query(Ana_test).all()
    print('ana_test table data: \n', [str(index) + ' = ' + query_obj.name for index, query_obj in enumerate(ana_query)])
    # 关闭session
    session.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 20:26
# @Author  : RookieDay
# @Site    : 
# @File    : README.py
# @Software: PyCharm Community Edition

# ORM框架是SQLAlchemy
from sqlalchemy import Column, String, create_engine, Integer, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()

# 定义USER对象  创建一个与数据库中的users表匹配的python类
class User(Base):
    # 表的名字
    __tablename__ = 'user'
    # 表的结构
    id = Column(Integer, Sequence('id'),primary_key=True)
    name = Column(String(20))

# 初始化数据库链接
# mysql_engine = create_engine("$address", echo, module)
#address 数据库://用户名:密码（没有密码则为空）@主机名：端口/数据库名
# echo标识用于设置通过python标准日志模块完成的SQLAlchemy日志系统，当开启日志功能，我们将能看到所有的SQL生成代码
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型 后台数据库的具体实现交由session完成
DBSession = sessionmaker(bind=engine)

# 关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
# 向数据库表中添加一行记录，可以视为添加一个User对象
# 创建session对象
session = DBSession()
# 创建新的user对象
new_user = User(name='ana')
# 添加到seesion
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
u1 = session.query(User).filter(User.id=='6').one()
print(u1.id)
print(u1.name)
print(type(u1))
# 关闭session
session.close()


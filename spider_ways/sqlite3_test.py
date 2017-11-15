#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15
# @Author  : RookieDay
# @Site    : 
# @File    : sqlite3_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 参考
# http://www.runoob.com/sqlite/sqlite-python.html
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql = 'create table user (' \
      'id varchar(20) primary key, ' \
      'name varchar(20))'

cursor.execute(sql)

insert_sql = 'insert into user (id, name) ' \
             'values (\'1\', \'Michael\')'
cursor.execute(insert_sql)
print(cursor.rowcount)
conn.commit()

sql = 'select * from user where id=?', ('1',)
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集:
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
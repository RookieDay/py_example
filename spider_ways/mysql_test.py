#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15
# @Author  : RookieDay
# @Site    : 
# @File    : mysql_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
import mysql.connector

# 打开数据库连接
db = mysql.connector.connect(user='root',password='123456',database='ana_db')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用 execute() 方法执行 SQL，如果表存在则删除
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         ID INT PRIMARY KEY,
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(ID,FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES (1,'Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      fname = row[1]
      lname = row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
       # 打印结果
      print ("id=%d,fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (id,fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()


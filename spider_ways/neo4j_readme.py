#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16
# @Author  : RookieDay
# @Site    : 
# @File    : neo4j_readme
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# by https://www.w3cschool.cn/neo4j
# CREATE命令语法
# CREATE (
#    <node-name>:<label-name>
#    {
#       <Property1-name>:<Property1-Value>
#       ........
#       <Propertyn-name>:<Propertyn-Value>
#    }
# )

#     语法元素                                        	描述
# <node-name>	                            它是我们将要创建的节点名称。
# <label-name>	                            它是一个节点标签名称
# <Property1-name>...<Propertyn-name>	    属性是键值对。 定义将分配给创建节点的属性的名称
# <Property1-value>...<Propertyn-value>	    属性是键值对。 定义将分配给创建节点的属性的值
# CREATE (emp:Employee{id:123,name:"Lokesh",sal:35000,deptno:10})

# MATCH命令用于 -
# 从数据库获取有关节点和属性的数据
# 从数据库获取有关节点，关系和属性的数据
# MATCH
# (
#    <node-name>:<label-name>
# )

# RETURN子句用于 -
# 检索节点的某些属性
# 检索节点的所有属性
# 检索节点和关联关系的某些属性
# 检索节点和关联关系的所有属性
# RETURN
#    <node-name>.<property1-name>,
#    ........
#    <node-name>.<propertyn-name>

# CQL MATCH + RETURN命令 -
# 检索节点的某些属性
# 检索节点的所有属性
# 检索节点和关联关系的某些属性
# 检索节点和关联关系的所有属性
# MATCH (dept: Dept)
# RETURN dept.deptno,dept.dname


# 我们将创建两个节点：客id，name，dob属性。
# 客户节点包含：ID，姓名，出生日期属性
# CreditCard节点包含：id，number，cvv，expiredate属性
# 客户与信用卡关系：DO_SHOPPING_WITH
# CreditCard到客户关系：ASSOCIATED_WITH
#
# 我们将在以下步骤中处理此示例： -
# 创建客户节点
# 创建CreditCard节点
# 观察先前创建的两个节点：Customer和CreditCard
# 创建客户和CreditCard节点之间的关系
# 查看新创建的关系详细信息
# 详细查看每个节点和关系属性

# 创建两个节点
# CREATE (e:Customer{id:"1001",name:"Abc",dob:"01/10/1982"})
# CREATE (cc:CreditCard{id:"5001",number:"1234567890",cvv:"888",expiredate:"20/17"})
# 查看客户节点详细信息
# MATCH (e:Customer)
# RETURN e.id,e.name,e.dob
# 查看CreditCard节点详细信息
# MATCH (cc:CreditCard)
# RETURN cc.id,cc.number,cc.cvv,cc.expiredate


# 多个标签到节点
# CREATE (<node-name>:<label-name1>:<label-name2>.....:<label-namen>)
# CREATE (m:Movie:Cinema:Film:Picture)   m是一个节点名,movie, Cinema, Film, Picture是m节点的多个标签名称

# 单个标签到关系
# CREATE (<node1-name>:<label1-name>)-
# 	[(<relationship-name>:<relationship-label-name>)]
# 	->(<node2-name>:<label2-name>)


# 使用WHERE子句创建关系
# 创建两个现有节点之间的关系
# 一次创建两个节点和它们之间的关系
# 使用WHERE子句创建两个现有节点之间的关系
# MATCH (<node1-label-name>:<node1-name>),(<node2-label-name>:<node2-name>)
# WHERE <condition>
# CREATE (<node1-label-name>)-[<relationship-label-name>:<relationship-name>
#        {<relationship-properties>}]->(<node2-label-name>)

# MATCH (cust:Customer),(cc:CreditCard)
# WHERE cust.id = "1001" AND cc.id= "5001"
# CREATE (cust)-[r:DO_SHOPPING_WITH{shopdate:"12/12/2014",price:55000}]->(cc)
# RETURN r



# Neo4j-没有属性的关系与现有节点
# MATCH (<node1-label-name>:<node1-name>),(<node2-label-name>:<node2-name>)
# CREATE
# 	(<node1-label-name>)-[<relationship-label-name>:<relationship-name>]->(<node2-label-name>)
# RETURN <relationship-label-name>

# 建立关系
# MATCH (e:Customer),(cc:CreditCard)
# CREATE (e)-[r:DO_SHOPPING_WITH ]->(cc)

# 这里关系名称为“DO_SHOPPING_WITH”
# 关系标签为“r”。
# e和Customer分别是客户节点的节点名称和节点标签名称。
# cc和CreditCard分别是CreditCard节点的节点名和节点标签名。

# MATCH (e:Customer)-[r:DO_SHOPPING_WITH ]->(cc:CreditCard)
# RETURN r

# 现有节点的属性的关系
# MATCH (<node1-label-name>:<node1-name>),(<node2-label-name>:<node2-name>)
# CREATE
# 	(<node1-label-name>)-[<relationship-label-name>:<relationship-name>
# 	{<define-properties-list>}]->(<node2-label-name>)
# RETURN <relationship-label-name>

# MATCH (cust:Customer),(cc:CreditCard)
# CREATE (cust)-[r:DO_SHOPPING_WITH{shopdate:"12/12/2014",price:55000}]->(cc)
# RETURN r

# 关系名称为“DO_SHOPPING_WITH”
# 关系标签为“r”。
# shopdate和price是关系“r”的属性。
# e和Customer分别是客户节点的节点名称和节点标签名称。
# cc和CreditCard分别是CreditCard节点的节点名和节点标签名。


# 新节点无属性关系
# CREATE
#    (<node1-label-name>:<node1-name>)-
#    [<relationship-label-name>:<relationship-name>]->
#    (<node1-label-name>:<node1-name>)
# RETURN <relationship-label-name>

# CREATE (fb1:FaceBookProfile1)-[like:LIKES]->(fb2:FaceBookProfile2)
# 关系名称是“LIKES”
# 关系标签是“like”。
# fb1和FaceBookProfile1分别是“From Node”的节点名和节点标签名。
# fb2和FaceBookProfile2分别是“To Node”的节点名和节点标签名。

# MATCH (fb1:FaceBookProfile1)-[like:LIKES]->(fb2:FaceBookProfile2)
# RETURN like


# 新节点与属性的关系
# CREATE
# 	(<node1-label-name>:<node1-name>{<define-properties-list>})-
# 	[<relationship-label-name>:<relationship-name>{<define-properties-list>}]
# 	->(<node1-label-name>:<node1-name>{<define-properties-list>})
# RETURN <relationship-label-name>

# CREATE (video1:YoutubeVideo1{title:"Action Movie1",updated_by:"Abc",uploaded_date:"10/10/2010"})
# -[movie:ACTION_MOVIES{rating:1}]->
# (video2:YoutubeVideo2{title:"Action Movie2",updated_by:"Xyz",uploaded_date:"12/12/2012"})
# 这里的关系名称是“ACTION_MOVIES”
# 关系标签是“电影”。
# video1和YoutubeVideo1分别是“From Node”的节点名和节点标签名。
# video2和YoutubeVideo2分别是“To Node”的节点名和节点标签名。

# MATCH (video1:YoutubeVideo1)-[movie:ACTION_MOVIES]->(video2:YoutubeVideo2)
# RETURN movie


# 检索关系节点的详细信息
# MATCH
# (<node1-label-name>)-[<relationship-label-name>:<relationship-name>]->(<node2-label-name>)
# RETURN <relationship-label-name>

# MATCH (cust)-[r:DO_SHOPPING_WITH]->(cc)
# RETURN cust,cc

# DELETE子句
# 删除节点。
# 删除节点及相关节点和关系。
# DELETE <node-name-list>
# DELETE <node1-name>,<node2-name>,<relationship-name>

# REMOVE命令用于
# 删除节点或关系的标签
# 删除节点或关系的属性
#
# DELETE操作用于删除节点和关联关系。
# REMOVE操作用于删除标签和属性。

# REMOVE <property-name-list>
# CREATE (book:Book {id:122,title:"Neo4j Tutorial",pages:340,price:250})
#
# MATCH (book : Book)
# RETURN book
#
# MATCH (book { id:122 })
# REMOVE book.price
# RETURN book
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16
# @Author  : RookieDay
# @Site    : 
# @File    : neo4j_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# refer http://py2neo.org/2.0/
# by http://python.jobbole.com/84190/

from py2neo import Graph,Node,Relationship

test_graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

test_node_1 = Node(label = "Person",name = "test_node_1")
test_node_2 = Node(label = "Person",name = "test_node_2")
test_graph.create(test_node_1)
test_graph.create(test_node_2)

node_1_call_node_2 = Relationship(test_node_1,'CALL',test_node_2)
node_1_call_node_2['count'] = 1
node_2_call_node_1 = Relationship(test_node_2,'CALL',test_node_1)
node_2_call_node_1['count'] = 2
test_graph.create(node_1_call_node_2)
test_graph.create(node_2_call_node_1)


node_1_call_node_2['count']+=1
test_graph.push(node_1_call_node_2)

find_code_1 = test_graph.find_one(
  label="Person",
  property_key="name",
  property_value="test_node_1"
)
print (find_code_1)

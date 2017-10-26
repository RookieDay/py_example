#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 14:33
# @Author  : RookieDay
# @Site    : 
# @File    : README.py
# @Software: PyCharm Community Edition
# windows 安装redis
# 下载地址：https://github.com/MSOpenTech/redis/releases。
# redis模块

import redis
r = redis.Redis(host='localhost',port=6379,db=0)
r.set('hello','word')
print(r.get('hello'))

# 获取集合中所有的成员--迭代器的方式
# sscan_iter(name, match=None, count=None)
for i in r.sscan_iter('code',match=None,count=2):
    print(i)


# 参考：http://www.redis.net.cn/order/3528.html

# redis key
# DEL 命令用于删除已存在的键。不存在的 key 会被忽略
# 返回值:被删除 key 的数量。
# 语法：DEL KEY_NAME

# DUMP 命令用于序列化给定 key ，并返回被序列化的值。
# 返回值：如果 key 不存在，那么返回 nil 。 否则，返回序列化之后的值。
# 语法：DUMP KEY_NAME

# EXISTS 命令用于检查给定 key 是否存在。
# 返回值：若 key 存在返回 1 ，否则返回 0 。
# 语法：EXISTS KEY_NAME

# Expire 命令用于设置 key 的过期时间。key 过期后将不再可用。
# 返回值：设置成功返回 1 。 当 key 不存在或者不能为 key 设置过期时间时(比如在低于 2.1.3 版本的 Redis 中你尝试更新 key 的过期时间)返回 0 。
# 语法：Expire KEY_NAME TIME_IN_SECONDS
# SET w3ckey redis
# EXPIRE w3ckey 60
# 我们为键 w3ckey 设置了过期时间为 1 分钟，1分钟后该键会自动删除。

# Redis Expireat 命令
# Redis PEXPIREAT 命令
# Redis PEXPIREAT 命令
# Redis Keys 命令
# Redis Move 命令
# Redis PERSIST 命令
# Redis Pttl 命令
# Redis TTL 命令
# Redis RANDOMKEY 命令
# Redis Rename 命令
# Redis Renamenx 命令
# Redis Type 命令


# redis set
# Sadd 命令将一个或多个成员元素加入到集合中，已经存在于集合的成员元素将被忽略。
# 假如集合 key 不存在，则创建一个只包含添加的元素作成员的集合。
# 当集合 key 不是集合类型时，返回一个错误。
# 返回值：被添加到集合中的新元素的数量，不包括被忽略的元素。
# 语法：SADD KEY_NAME VALUE1..VALUEN

# Scard 命令返回集合中元素的数量。
# 返回值：集合的数量。 当集合 key 不存在时，返回 0 。

# Sdiff 命令返回给定集合之间的差集。不存在的集合 key 将视为空集。
# 返回值：包含差集成员的列表。

# Sdiffstore 命令将给定集合之间的差集存储在指定的集合中。如果指定的集合 key 已存在，则会被覆盖。
# 语法：SDIFFSTORE DESTINATION_KEY KEY1..KEYN
# SDIFFSTORE destset myset myset2 （destest 目标集合 myset集合1 myset2 集合2 返回myset和myset2的交集放到deset）
# 返回值：结果集中的元素数量。

# Sinter 命令返回给定所有给定集合的交集。 不存在的集合 key 被视为空集。 当给定集合当中有一个空集时，结果也为空集(根据集合运算定律)。
# 返回值：交集成员的列表

# Sinterstore 命令将给定集合之间的交集存储在指定的集合中。如果指定的集合已经存在，则将其覆盖。
# 语法：SINTERSTORE DESTINATION_KEY KEY KEY1..KEYN
# 返回值： 交集成员的列表。

# Sismember 命令判断成员元素是否是集合的成员。
# 语法：SISMEMBER KEY VALUE
# 返回值:如果成员元素是集合的成员，返回 1 。 如果成员元素不是集合的成员，或 key 不存在，返回 0 。

# Smembers 命令返回集合中的所有的成员。 不存在的集合 key 被视为空集合。
# 语法：SMEMBERS KEY VALUE
# 返回值：集合中的所有成员

# Smove 命令将指定成员 member 元素从 source 集合移动到 destination 集合。
# 如果 source 集合不存在或不包含指定的 member 元素，则 SMOVE 命令不执行任何操作，仅返回 0 。否则， member 元素从 source 集合中被移除，并添加到 destination 集合中去。
# 当 destination 集合已经包含 member 元素时， SMOVE 命令只是简单地将 source 集合中的 member 元素删除。
# 当 source 或 destination 不是集合类型时，返回一个错误。
# 语法：SMOVE SOURCE DESTINATION MEMBER
# 返回值：如果成员元素被成功移除，返回 1 。 如果成员元素不是 source 集合的成员，并且没有任何操作对 destination 集合执行，那么返回 0

# Spop 命令用于移除并返回集合中的一个随机元素。
# 语法:SPOP KEY
# 返回值：被移除的随机元素。 当集合不存在或是空集时，返回 nil

# Srandmember 命令用于返回集合中的一个随机元素。
# 从 Redis 2.6 版本开始， Srandmember 命令接受可选的 count 参数：
# 如果 count 为正数，且小于集合基数，那么命令返回一个包含 count 个元素的数组，数组中的元素各不相同。如果 count 大于等于集合基数，那么返回整个集合。
# 如果 count 为负数，那么命令返回一个数组，数组中的元素可能会重复出现多次，而数组的长度为 count 的绝对值。
# 该操作和 SPOP 相似，但 SPOP 将随机元素从集合中移除并返回，而 Srandmember 则仅仅返回随机元素，而不对集合进行任何改动。
# 语法：SRANDMEMBER KEY [count]
# 返回值：只提供集合 key 参数时，返回一个元素；如果集合为空，返回 nil 。 如果提供了 count 参数，那么返回一个数组；如果集合为空，返回空数组

# Srem 命令用于移除集合中的一个或多个成员元素，不存在的成员元素会被忽略。 当 key 不是集合类型，返回一个错误。
# 语法：SREM KEY MEMBER1..MEMBERN
# 返回值：被成功移除的元素的数量，不包括被忽略的元素。

# Sunion 命令返回给定集合的并集。不存在的集合 key 被视为空集。
# Sunionstore 命令将给定集合的并集存储在指定的集合 destination 中。

# SCAN基本用法：SCAN cursor
# SCAN是通过游标cursor来遍历集合的，遍历开始时设置为0，如果终止server 返回0，否则，返回cusor遍历的值，该值呈上升趋势且大于0。

# Sscan 命令用于迭代集合键中的元素。
# 语法：SSCAN KEY [MATCH pattern] [COUNT count]
# 返回值：数组列表。
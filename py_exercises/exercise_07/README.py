#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Software: PyCharm Community Edition
from collections import Counter
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict

# namedtuple part
# tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
# p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,3)
print(p.x, p.y)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
print(isinstance(p,Point))
print(isinstance(p,tuple))

print('-'*40)
# deque part
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
d = deque(['a','b','c'])
s1 = d.append('m')
print(d)
s2 = d.appendleft('q')
print(d)
s3 = d.pop()
print(d)


print('-'*40)
# defaultdict part
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

print('-'*40)
# OrderedDict part
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
k = dict([('a', 1), ('b', 2), ('c', 3)])
print(k)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
k1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(k1)
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


print('-'*40)
# Counter part
print(Counter())
print(Counter('ana'))
print(Counter({'a':3,'c':2}))
print(Counter(a=1,b=2))

print('-'*40)
# 当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。
c = Counter("abcdefgab")
print(c['a'], c['p'])

print('-'*40)
# 可以使用一个iterable对象或者另一个Counter对象来更新键值。
# 计数器的更新包括增加和减少两种。其中，增加使用update()方法
c.update('ppp') # 使用另一个iterable对象更新
print(c, c['h'])
d = Counter('wwwa')
c.update(d)
print(c, c['w'])

print('-'*40)
# 减少则使用subtract()方法：
c.subtract('ppp') # 使用另一个iterable对象更新
print(c, c['h'])
m = Counter('ww')
c.subtract(m)
print(c, c['w'])

print('-'*40)
# 当计数值为0时，并不意味着元素被删除，删除元素应当使用del
m = Counter("abcdcba")
print(m)
m["b"] = 0
print(m)
del m['b']
print(m)

print('-'*40)
# elements() 返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。元素排列无确定顺序，个数小于1的元素不被包含。
k = Counter(a=4, b=2, c=0, d=-2)
print(list(k.elements()))

print('-'*40)
# most_common([n]) 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。
s = Counter('abracaowksdapodiqpdabra')
print(s.most_common())
print(s.most_common(2))

print('-'*40)
# 浅拷贝copy
x = Counter('apodiqpdabra')
print(x)
print(x.copy())

print('-'*40)
# +、-、&、|操作也可以用于Counter。其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。需要注意的是，得到的Counter对象将删除小于1的元素。

print('-'*40)
j = Counter(a=3, b=1)
l = Counter(a=1, b=2)
print(j + l)
print(j - l) #只保留正数计数的元素
print(j & l)
print(j | l )

print('-'*40)
print(sum(c.values())) # 所有计数的总数
print(c.clear())  # 重置Counter对象，注意不是删除
print(c)
print(m)
print(list(m)) # 将c中的键转为列表
print(set(m)) # 将c中的键转为set
print(dict(m)) # 将c中的键值对转为字典
print(m.items()) # 转为(elem, cnt)格式的列表
print(Counter(dict(m.items()))) # 从(elem, cnt)格式的列表转换为Counter类对象
# print(m.most_common()[:-n:-1]) # 取出计数最少的n-1个元素
m += Counter() # 移除0和负值
print(m)


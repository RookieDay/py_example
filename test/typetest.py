#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:34
# @Author  : RookieDay
# @Site    : 
# @File    : typetest.py
# @Software: PyCharm Community Edition


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass

print(type(fn) == types.FunctionType)

# isinstance()就可以告诉我们，一个对象是否是某种类型
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)

# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法
len('ABC')
'ABC'.__len__()

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('ABC'))


# type()函数可以查看一个类型或变量的类型
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

# 方法
# 要创建一个class对象，type()函数依次传入3个参数：
#   class的名称；
#   继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#   class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# __new__()方法接收到的参数依次是：
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。

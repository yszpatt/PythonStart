#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-19 21:50:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# self的使用方式


class Ball():
    """docstring fos Ball"""

    def setName(self, name):
        self.name = name

    def kick(self):
        print('我叫 %s 谁踢我' % self.name)


a = Ball()
a.setName('球A')
c = Ball()
c.setName('球C')
a.kick()
c.kick()

# init魔法方法类似构造函数，初始化时自动加载


class Ball():
    """docstring for Ball"""

    def __init__(self, name):
        self.name = name

    def kick(self):
        print('我叫 %s 谁踢我' % self.name)


b = Ball('土豆')
b.kick()

# python中的私有，变量或函数名前加__表示私有


class Person():
    __name = '私有名'

    def getName(self):
        return self.__name


d = Person()
print(d.getName())
print(d._Person__name)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-27 22:18:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class CapStr(str):
    # 在init前调用，参数传init
    def __new__(cls, string):
        print('__new__调用')
        string = string.upper()
        return str.__new__(cls, string)

    # 构造，初始化
    def __init__(self, b):
        print('__init__调用：', b)
        self.x = 4
        self.y = 5

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return (self.x * self.y)

    # 析构函数
    def __del__(self):
        print('所有相关引用被调用，垃圾回收__del__')


a = CapStr('string')
print(a.getArea())
print(a.getPeri())
print(a)
del a

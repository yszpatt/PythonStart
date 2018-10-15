#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 22:05:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size
        # property直接关联属性
    x = property(getSize, setSize, delSize)


c = C()
print(c.x)
c.x = 1
print(c.x)


class M:
    # 属性被访问调用
    def __getattribute__(self, name):
        print("getattribule")
        return super().__getattribute__(name)
# 获取不存在的属性时调用

    def __getattr__(self, name):
        print("getattr")
# 属性被设置时调用

    def __setattr__(self, name, value):
        print("setattr")
        super().__setattr__(name, value)
# 删除时调用

    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)


m = M()
m.x
m.x = 1
m.x

# 魔方方法直接访问属性的无限循环


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # 这个位置 出现死循环
            super().__setattr__(name, value)
            self.__dict__[name] = value

    def getArea(self):
        print(self.width * self.height)


r = Rectangle(4, 5)
r.getArea()
r.square = 10
r.getArea()
print(r.width)
print(r.height)
# 使用—dict以字典形式管理所有属性
print(r.__dict__)

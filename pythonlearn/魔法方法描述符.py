#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 21:49:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class MyDeciptor:
    def __get__(self, instance, owner):
        print("getting....", self, instance, owner)

    def __set__(self, instance, value):
        print("setting....", self, instance, value)

    def __delete__(self, instance):
        print("deleting....", self, instance)


class Test:
    x = MyDeciptor()
    # MyDeciptor是test描述符类


test = Test()
test.x
test.x = 1
del test.x


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        return self.fset(instance, value)

    def __delete__(self, instance):
        return self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


c = C()
c.x = 'X-Man'
print(c.x)
print(c._x)

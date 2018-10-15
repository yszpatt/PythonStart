#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-19 22:08:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import random as r


class Parent():
    def Hello(self):
        print('正在调用父类方法')


class Child(Parent):
    pass


c = Child()
c.Hello()


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('鱼的位置是', self.x, self.y)


class Shake(Fish):
    def __init__(self):
        # 调用父类中未绑定的方法一
        # Fish.__init__(self)
        # 使用super 方法
        super().__init__()
        self.is_hungry = True

    def eat(self):
        if self.is_hungry:
            print('饿了吃东西')
            self.is_hungry = False
        else:
            print('刚吃完')

# 多重继承


class Ass(Fish, Parent):
    pass


shake = Ass()
shake.move()
shake.Hello()

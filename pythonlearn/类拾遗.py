#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-20 20:23:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('池子里有乌龟：%d ，鱼：%d' % (self.turtle.num, self.fish.num))


pool = Pool(1, 24)
pool.print_num()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 13:14:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

string = "JingDong"
it = iter(string)

# for工作原理

while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


class Fibs():
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


Fibs = Fibs(100)
for each in Fibs:
    print(each)

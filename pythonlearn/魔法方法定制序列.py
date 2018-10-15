#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 22:22:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数


class CountList:
    def __init__(self, *args):
        # 列表推导式
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        print("调用__len__")
        return len(self.values)

    def __getitem__(self, key):
        print("调用__getitem__")
        self.count[key] += 1
        return self.values[key]


c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1[1])
print(c2[1])
print(c1[1] + c2[1])
print(c1.count)
print(c2.count)
print(len(c1))

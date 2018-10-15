#!/usr/bin/env python
# coding:utf-8
# 题目：将一个列表的数据复制到另一个列表中。

a = [1, 2, 3]
b = a[:]
print(b)


l = [1, 2, 3, 4, 5]
p = []
for i in range(len(l)):
    p.append(l[i])
print(p)

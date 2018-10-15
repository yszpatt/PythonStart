#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 统计 1 到 100 之和。
import functools

n = 0
for i in range(1, 101):
    n += i

print(n)

y = functools.reduce(lambda x, y: x + y, range(1, 101))
print(y)

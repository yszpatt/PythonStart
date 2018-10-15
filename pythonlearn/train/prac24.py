#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。


s = 0
a = 2
b = 1
for i in range(0, 21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 求1+2!+3!+...+20!的和。


s = 0
t = 1
for i in range(1, 21):
    t *= i
    s += t
print(s)

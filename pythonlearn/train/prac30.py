#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


s = int(input('请输入5位数字:'))
print(len(str(s)))
x = []
for i in range(1, len(str(s)) + 1):
    x.append(int(s % 10))
    s /= 10

if (x[0] == x[-1]) and x[1] == x[-2]:
    print('回文数')
else:
    print('非回文数')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


s = int(input('请输入5位数字:'))
print(len(str(s)))
x = []
for i in range(1, len(str(s)) + 1):
    x.append(int(s % 10))
    s /= 10
print(x)

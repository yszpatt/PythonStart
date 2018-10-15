#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 求输入数字的平方，如果平方运算后小于 50 则退出。

n = int(input("输入一个数字："))
i = n ** 2
if(i <= 50):
    quit()
else:
    print(i)

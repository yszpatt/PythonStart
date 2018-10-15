#!/usr/bin/env python
# coding:utf-8
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

import functools

a = int(input("输入数字a:"))
n = int(input("输入数字n:"))
Sn = []
Tn = 0
x = 0
for i in range(0, n):
    Tn = Tn + a
    a = 10 * a
    Sn.append(Tn)
print(Sn)

print(functools.reduce(lambda x, y: x + y, Sn))

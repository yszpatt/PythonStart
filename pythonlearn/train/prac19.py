#!/usr/bin/env python
# coding:utf-8
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6 = 1＋2＋3.编程找出1000以内的所有完数。


list1 = []
for i in range(2, 1001):
    list2 = []
    for n in range(1, int(i / 2) + 1):
        if i % n == 0:
            list2.append(n)
    # print(list2)

    if i == sum(list2):
        print(i)
        print(list2)

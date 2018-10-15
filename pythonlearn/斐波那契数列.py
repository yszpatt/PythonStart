#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-05 17:00:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 迭代写法


def feibodiedai(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入错误')
        return -1
    while (n - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3


# 递归写法
def feibodigui(n):
    if n < 1:
        print('输入错误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return feibodigui(n - 2) + feibodigui(n - 1)

# 迭代输出整个数列


def fibo(num):
    numList = [0, 1]

    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList


number = int(input('输入正整数：'))
result = fibo(number)
print(result)
# print('%d 的数列值是：%d' % (number, result))

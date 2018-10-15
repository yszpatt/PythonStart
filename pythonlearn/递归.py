#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-05 11:14:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 求阶乘 非递归版本


# def factorial(n):
#     result = n
#     for i in range(1, n):
#         result *= i
#     return result


# 递归版本
def factorial1(n):
    if n == 1:
        return 1
    else:
        return n * (factorial1(n - 1))


number = int(input('输入正整数'))
result = factorial1(number)
print('%d 的阶乘是：%d' % (number, result))

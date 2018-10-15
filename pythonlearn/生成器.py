#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 13:35:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


def myGen():
    print("生成器被执行")
    # yield相当于return，根据next一次执行，最后返回stopInteratrion
    yield 1
    yield 2


mG = myGen()
print(next(mG))
print(next(mG))
# print(next(mG))

# 生成器完成斐波那契数列


def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in libs():
    if each > 100:
        break
    else:
        print(each, end=' ')

# 列表推导式 能被2整除不能被3整除
a = [i for i in range(100) if not (i % 2) and i % 3]
print(a)

# 字典推导式 能否被2整除
b = {i: i % 2 == 0 for i in range(100)}
print(b)

# 集合推导式,去重复
c = {i for i in [1, 2, 3, 5, 6, 2, 3, 6, 17, 7, 1, 3, 5, ]}
print(c)

# 没有元祖推导式与字符推导式
# 生成器推导式
e = (i for i in range(100))
print(e)
print(next(e))
print(next(e))
# 生成器推导式作为参数，求和100内不能被2整除的数
print(sum(i for i in range(100) if i % 2))

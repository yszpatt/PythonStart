#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-03 21:50:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 全局变量在函数内修改的机制
count = 5


def myfun():
    count = 10
    print(count)


myfun()
print(count)

# global关键字修改全局变量


def myfun1():
    global count
    count = 10
    print(count)


myfun1()
print(count)

# 内嵌函数


def function1():
    print('function1')

    def function2():
        print('function2')
    function2()


function1()

# 闭包，如下例子中funY为闭包


def funX(x):
    def funY(y):
        return x * y
    return funY


# 闭包的调用方式
i = funX(8)
print(i)
print(i(5))
print(funX(3)(5))


# 关键字nonlocal，降调非本地函数，用于闭包时使用
def fun1():
    x = 5

    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()


print(fun1())

# 匿名函数


def ds(x):
    return 2 * x + 1


print(ds(5))
# lambda关键字，自动生成函数，不需要考虑命名问题，可精简代码
lambda x, y: 2 * x + 1 + y
# filter过滤器，返回列表中为true的值，或函数以列表中的值为参数的返回值为true的参数值
# 过滤偶数


def odd(x):
    return x % 2


temp = range(10)
show = (filter(odd, temp))
print(list(show))

# 结合limbda和filter的简单写法
# map函数，列出所有返回值
filter1 = list(filter(lambda x: x % 2, range(10)))
map1 = list(map(lambda x: x * 2, range(10)))
print(filter1)
print(map1)

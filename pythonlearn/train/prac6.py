#!/usr/bin/env python
# coding:utf-8
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)


def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 11):
    print(fib(i))


def fib2(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出了第10个斐波那契数列
print(fib2(10))

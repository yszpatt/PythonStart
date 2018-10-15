#!/usr/bin/env python
# coding:utf-8
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = int(input("输入正整数n:"))
print("%d = " % n, end='')
while n not in [1]:
    for k in range(2, n + 1):
        if n % k == 0:
            n = int(n / k)
            if n == 1:
                print("%d " % k, end='')
            else:
                print("%d * " % k, end='')
            break
print()

# x = int(input("是否进入循环？是：1， 否：0\n"))
# while(x):
#     n = int(input("请输入一个正整数："))
#     print("%d = " % n, end='')
#     while n not in [1]:
#         for index in range(2, n + 1):
#             if n % index == 0:
#                 n = int(n / index)
#                 if n == 1:
#                     print("%d " % index, end='')
#                 else:
#                     print("%d * " % index, end='')
#                 break
#     print()
#     x = int(input("是否进入循环？是：1， 否：0\n"))

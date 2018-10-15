#!/usr/bin/env python
# coding:utf-8
# 利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码

import random


def randomKey1(numb):
    tmp = ''
    for x in range(0, numb):
        n = random.randint(0, 2)
        if n == 0:
            num = random.randint(97, 122)
            num = chr(num)
            tmp += num
        else:
            num = random.randint(0, 9)
            tmp += str(num)
    return tmp


def randomKey2(numb):
    tmp = ''
    for x in range(0, numb):
        num = random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        # if num >= 58 and num <= 96:
        #     print("无效符号")
        tmp += num

    return tmp


print(randomKey1(4))
print(randomKey2(4))

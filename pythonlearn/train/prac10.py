#!/usr/bin/env python
# coding:utf-8
# 暂停一秒输出，并格式化当前时间


import time
j = int(input("输入暂停时间："))
print(time.strftime("%H:%M:%S %Y-%m-%d", time.localtime()))
time.sleep(j)
print("计时时间到")
print(time.strftime("%H:%M:%S %Y-%m-%d", time.localtime()))

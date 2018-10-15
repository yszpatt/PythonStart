#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天？

year = int(input("年："))
month = int(input("月："))
day = int(input("日："))

p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年
w = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年


if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    d = w
else:
    d = p

days = sum(d[0:month - 1]) + day
print("%d-%d-%d是一年中的第%d天" % (year, month, day, days))
print(d)

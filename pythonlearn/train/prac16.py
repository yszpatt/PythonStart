#!/usr/bin/env python
# coding:utf-8
# 输出指定格式的日期。


import time
import datetime

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1941, 1, 5))

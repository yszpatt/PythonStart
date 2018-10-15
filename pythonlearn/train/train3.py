#!/usr/bin/env python
# coding:utf-8
# 使用for循环实现输出2-3+4-5+6.....+100的和

sum = 0
i = 0
for i in range(2, 101):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i
    i += 1
print(sum)

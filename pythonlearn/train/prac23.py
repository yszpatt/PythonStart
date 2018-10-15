#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 打印出如下图案（菱形）


print('*')
print(' ')


def diamond(line):
    middle = int(line / 2)
    for i in range(1, line + 1):
        empty = abs(i - middle - 1)
        dia = abs(line - 2 * empty)
        print(' ' * empty, '*' * dia)


diamond(100)

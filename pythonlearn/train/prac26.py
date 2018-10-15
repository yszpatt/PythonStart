#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 利用递归方法求5!,递归公式：fn=fn_1*4!


def jx(lin):
    if lin == 1:
        return 1
    else:
        return lin * jx(lin - 1)


print(jx(5))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-01 20:45:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 创建一个元组
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[2])
print(tuple1[:5])
print(tuple1[2:])
tuple2 = tuple1[:]
# 元组不能被修改
# tuple1[0] = 3
# 创建空元组,","决定了是否创建的是元组
tuple3 = ()
tuple4 = 1, 2,
print(tuple4)
# 更新和删除一个元组，分片
temp = ("字符串1", "字符串2", "字符串3", "字符串4")
temp = temp[:2] + ("字符串插入",) + temp[2:]
print(temp)
# 删除元组 del temp

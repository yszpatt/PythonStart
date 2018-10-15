#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-30 20:57:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

favourite = ['FishC', '加油小胖子', '肚子精']
for e in favourite:
    print(e, len(e))
for x in range(2, 20, 3):
    print(x)
    if x > 10:
        break

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)

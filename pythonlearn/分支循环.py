#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-30 20:44:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

score = int(input('请输入分数:'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('B')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13 21:10:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

f = open('record.txt')

a = []
b = []
count = 1

for eachline in f:
    (role, line_spoken) = eachline.split(':', 1)
    if role == 'a':
        a.append(line_spoken)
    if role == 'b':
        b.append(line_spoken)


file_name_a = 'a_' + str(count) + '.txt'
file_name_b = 'b_' + str(count) + '.txt'

a_file = open(file_name_a, 'w')
b_file = open(file_name_b, 'w')

a_file.writelines(a)
b_file.writelines(b)

a_file.close()
b_file.close()

a = []
b = []
count += 1

f.close()

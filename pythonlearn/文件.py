#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13 13:25:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


f = open('record.txt', encoding='utf-8')
print(f.read())
print(f.tell(), '\n')
f.close()
f = open('record.txt', encoding='utf-8')
print(f.read(5))
print(f.tell(), '\n')

# 移动文件指针
f.seek(0, 1)
print(f.read(), '\n')

f.seek(0, 0)
print(f.readline())

print(list(f), '\n')

# 输出每一行
f.seek(0, 0)
# lines = list(f)
for eachline in f:
    print(eachline)

# 文件的写入
f.close()
f = open('writefile.txt', 'w', encoding='utf-8')
f.write('Write The File!\n')

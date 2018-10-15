#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-01 21:17:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

str1 = 'randOm'
str1 = str1.casefold()
print(str1)
print(str1)

str2 = "{0} love {1}.{2}".format("I", "FishC", "com")
print(str2)
str3 = "{a} love {b}.{c}".format(a="I", b="FishC", c="com")
print(str3)
# {{为转义
str4 = "{{0}}".format("test")
print(str4)
# 格式化符号：，打印1位定点数
print('{0:.1f}{1}'.format(27.664, 'GB'))
# 字符串可视化符号
# %c 格式化字符及其ASCII码
# %s 格式化字符串
# %d 格式化整数
# %o 格式化无符号八进制
# %x 格式化无符号十六进制
# %X 格式化无符号十六进制大写
# %f 格式化定点数，可制定小数点后精度
# %e 科学记数法格式化定点数
# %E 同上
# %g 根据值的大小自动使用%f或%e
# %G 同上

# 辅助指令
# m.n 最小总宽度m，小数点后n
# - 左对齐
# + 正数前显示+
# # 八进制前显示0，十六进制显示0x
# 0 数字前显示0替代空格

print('%#010X' % 65535)

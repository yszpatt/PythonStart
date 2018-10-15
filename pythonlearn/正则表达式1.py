#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 21:05:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
print(re.search(r'FishC', 'i Love FishC.com'))

# 正则通配符‘.’
print(re.search(r'.', 'i Love FishC.com'))
# 原字符标识‘\’
print(re.search(r'\.', 'i Love FishC.com'))
# 数字字符标识‘\d’
print(re.search(r'\d\d', 'i Love 12FishC.co4m'))

print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.101.111'))
# 创建字符类[]
print(re.search(r'[aeiou]', 'playwithevery'))
# [a-z]表示范围
print(re.search(r'[a-z]', 'playwithevery'))
# {3,5}表示次数
print(re.search(r'ab{3,5}c', 'abbbc'))

print(re.search(r'[0-255]', '188'))
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '018'))
print(re.search(
    r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])', '192.168.13.223'))
print(re.search(
    r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '254.132.3.23'))
print(re.search(
    r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))', '254.132.3.23'))

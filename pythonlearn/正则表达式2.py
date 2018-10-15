#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 23:17:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re

print(re.search(r"Fish(C|D)", "FishD"))
print(re.search(r"^FishC", "love FishC"))
print(re.search(r"^FishC", "FishClove"))
print(re.search(r"FishC$", "love FishC"))
# \1-\99表示第一个组 \000表示八进制
print(re.search(r"(FishC)\1", "love FishC"))
print(re.search(r"(FishC)\1", "FishCFishC"))

print(re.findall(r"[a-z]", "FishC.com"))
# ^脱字符取反
print(re.findall(r"[^a-z]", "FishC.com"))

print(re.search(r"FishC{3,4}", "FishCCCC.com"))

print(re.search(r"FishC{3,4}", "FishCCCC.com"))

# ？等价于{0，1}
# *等价于{0，}
# +等价于{1，}

s = "<html><title>I love FishC.com</title></html>"
# 贪婪模式
print(re.search(r"<.+>", s))
# 非贪婪模式
print(re.search(r"<.+?>", s))

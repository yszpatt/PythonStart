#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 23:40:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
# \b单词边界
print(re.findall(r"\bFishC\b", "FishC.com!cFishCcom!(FishC"))
print(re.findall(r"\BFishC\B", "FishC.com!cFishCcom!(FishC"))
# \s空白字符
print(re.findall(r"\sFishC\s", "FishC.com! FishC com!(FishC)"))
print(re.findall(r"\SFishC\S", "FishC.com! FishC com!(FishC)"))
# \w 单词字母
print(re.findall(r"\wFishC\w", "FishC.com! aFishCb com!(FishC"))
print(re.findall(r"\WFishC\W", "FishC.com! FishC com!(FishC"))

# 编译正则表达式
p = re.compile(r"[a-z]")
print(type(p))
print(p.findall("FishC.com! FishC com!(FishC", re.L))
# 编译标志

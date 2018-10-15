#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 20:38:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request

reg = urllib.request.Request('http://placekitten.com')
response = urllib.request.urlopen(reg)
cat_img = response.read()


# with open('cat_300_602.jpg', 'wb') as f:
#     f.write(cat_img)

# 爬取网页源码
print(cat_img.decode("utf-8"))

# 爬取网页图片
reg = urllib.request.Request('http://placekitten.com/g/300/602')
response = urllib.request.urlopen(reg)
cat_img = response.read()

with open('cat_300_602.jpg', 'wb') as f:
    f.write(cat_img)

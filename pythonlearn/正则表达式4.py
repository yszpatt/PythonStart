#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-18 20:00:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import re

result = re.search(r"(\w+) (\w+)", "i love fishC.com")
print(result)
print(result.group())
print(result.end())
print(result.span())


# 百度贴吧
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")

    print(url)
    return html


def get_img(html):
    p = r'<img src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    for each in imglist:
        print(each)
    # for each in imglist:
    #     filename = each.split("/")[-1]
    #     urllib.request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = 'http://www.3dmgame.com/zt/201806/3737575.html'
    get_img(url_open(url))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 14:30:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 代理 参数是一个字典{类型：‘代理ip：端口号’}
# proxy_support = rullib.request.ProxyHandler({})
# 定义创建一个opener，应用代理
# opener = urllib.request.build_opener(proxy_support)
# 安装opener
# urllib.request.install_opener(opener)
# 或者调用opener
# opener.open(url)


import urllib.request

url = 'http://ip.chinaz.com/'

proxy_support = urllib.request.ProxyHandler({'http': '171.39.200.13:808'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')


print(html)

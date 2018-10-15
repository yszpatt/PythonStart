#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 21:04:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import urllib.parse
import json
import time

while True:
    inp = input("输入翻译的内容(输入q退出程序)：")
    while inp == '':
        inp = input("输入内容无效，请重新输入(输入q退出程序)：")
    else:
        content = inp
    if content == 'q':
        break

    url = 'http://fanyi.youdao.com/translate'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1528894849481'
    data['sign'] = 'e84d12d8cbc63c557da669f98c79aa4f'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    # date字符串转换，将URL拆分
    data = urllib.parse.urlencode(data).encode('utf-8')
    # print(data)
    # 声明Request，增加header
    req = urllib.request.Request(url, data, head)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    # json解析
    target = json.loads(html)
    print('翻译结果：%s' % target['translateResult'][0][0]['tgt'])
    time.sleep(5)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 15:39:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    print(url)
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    print(html[a:b])
    return '11'


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('<img class="picact" border="0" alt="游民星空" src=')
    while a != -1:
        b = html.find('.gif', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 47:b + 4])
        else:
            b = a + 47
        a = html.find('<img class="picact" border="0" alt="游民星空" src=', b)
    for each in img_addrs:
        print(each)
    return img_addrs


def save_imgs(img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f. write(img)


def download_mm(folder='ooxx', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://www.gamersky.com/ent/201806/1061812_'
    # page_num = int(get_page(url))
    page_num = 12

    for i in range(pages):
        page_num -= 1
        page_url = url + str(page_num) + '.shtml'
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)


if __name__ == '__main__':
    download_mm()

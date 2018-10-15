#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-18 20:31:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import urllib.error

req = urllib.request.Request("http://www.ooxx-fichc.com")

try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)

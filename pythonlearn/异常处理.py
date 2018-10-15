#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-19 15:48:28
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

try:
    int('fff')
    sum = 1 + '1'
    f = open('文件名.txt')
    print(f.read())
    f.close
except OSError as reason:
    print('文件不存在 \n错误原因是', str(reason))
except TypeError as reason:
    print('类型出错 \n错误原因是', str(reason))

finally:
    print('最终执行')
    raise ZeroDivisionError('打印异常')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-05 23:22:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '---->', z)
    else:
        # 将前n-1个盘子移动到y上
        hanoi(n - 1, x, z, y)
        # 将最底下的盘子移动到z上
        print(x, '---->', z)
        # 将y上的n-1个盘子移动到z上
        hanoi(n - 1, y, x, z)


n = int(input('输入汉诺塔高度：'))
hanoi(n, 'X', 'Y', 'Z')

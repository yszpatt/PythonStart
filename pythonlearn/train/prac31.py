#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

letter1 = input('输入星期几第一个字母：')

weeklist = {'M': 'Monday', 'T': {'u': 'Tuesday', 'h': 'Thursday'},
            'W': 'Wednesday', 'F': 'Friday', 'S': {'a': 'Saturday', 'u': 'Sunday'}}

letter1 = letter1.upper()

if(letter1 in ['T', 'S']):
    letter2 = input('输入第二个字母')
    try:
        print(weeklist[letter1][letter2])
    except KeyError:
        print('输入错误')
    else:
        pass

else:
    try:
        print(weeklist[letter1])
    except KeyError:
        print('输入错误')
    else:
        pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 按逗号分隔列表。

list_ = [1, 2, 3, 4, 5]
print(list_)
list_ = repr(list_)[1:-1]
print(list_)
print(type(list_))


list_ = [1, 2, 3, 4, 5]
for i in range(0, len(list_)):
    if i != (len(list_) - 1):
        print(list_[i], end=',')
    else:
        print(list_[i])


list_ = [1, 2, 3, 4, 5]
str_ = ''
for i in range(0, len(list_) - 1):
    str_ += str(list_[i]) + ','

print(str_[0:-1])

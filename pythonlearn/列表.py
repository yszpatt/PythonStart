#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-30 20:57:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

mix = [1, 2, 'ffwef', 3, [33, 4]]
len(mix)  # 数组长度
mix.append(3333)    # 列表最后插入元素
mix.extend(['test', 222])  # 列表最后插入数组
mix.insert(0, '中文')  # 在特定位置插入
mix.count(2)    # 数组计数为2的元素
mix.index('中文')  # 查找对应元素在列表中的索引
mix.remove('中文')    # 在列表中移除元素
name = mix.pop(1)   # 提取索引数据，并在列表中删除
del mix[2]  # 清楚数组数据
mix.clear()  # 清楚列表中的所有元素
mix[1:3]    # 分片
print(mix)


# 数组比较
list1 = [123, 234]
list2 = [432, 123]
list1 < list2    # 数组比较，只比较第一个内容
lsit3 = [123, 234]
list1 = lsit3    # 数组取等
list4 = list1 + lsit3   # 数组叠加
print(list4)
list2 *= 3
print(list2)
print(123 in list2)  # 是否在列表
list5 = [1, 2, 3, 2, [4, 5, 6]]
print(list5[4][2])   # 二维数组索引

print(list5.count(2))  # 列表计数
print(list2.index(123, 2, 6))    # 列表索引，123在列表中的位置，从第3个数据起到第7个数据止
list5.reverse()      # 原地翻转列表
print(list5)
list6 = [1, 5, 29, 566, 384, 74, 2, 11, 5]
list6.sort(reverse=True)  # 列表排序，sort( func, key, reverse )
print(list6)
list7 = list6[:]  # 创建列表的拷贝
list8 = list6   # 分片与拷贝的区别：list8保持与list6相同
list6.sort()
print(list7)
print(list8)

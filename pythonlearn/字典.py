#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-12 19:18:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 使用数组模拟使用
brand = ['李宁', '耐克', '阿迪达斯', '工作室']
slogan = ['一切皆有可能', 'just do it', 'impossible is nothing', '让编程改变世界']
print('工作室的口号是：', slogan[brand.index('工作室')])


# 以字典方式实现 字典 花括号
dict1 = {'李宁': '一切皆有可能', '耐克': 'just do it',
         '阿迪达斯': 'impossible is nothing', '工作室': '让编程改变世界'}
print('工作室的口号是：', dict1['工作室'])
# 以key方式创建
dict2 = dict(小甲鱼='让编程改变世界', 李宁='一切皆有可能')
# 字典赋值
dict2['小甲鱼'] = '改变键值测试'
dict2['小甲'] = '新增键值测试'
print(dict2['小甲鱼'])
print(dict2['小甲'])

# 生成新字典
dict2 = dict2.fromkeys((1, 3), '数字')
print(dict2)
dict2 = dict2.fromkeys(range(0, 32), '赞')
print(dict2)

# 关键字key(),values(),items()
for eachKey in dict2.keys():
    print(eachKey)
for eachValues in dict2.values():
    print(eachValues)
for eachItems in dict2.items():
    print(eachItems)

# get方法访问字典的项
print(dict1.get(32))

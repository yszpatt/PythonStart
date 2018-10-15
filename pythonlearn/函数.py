#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 22:16:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 定义一个函数


def function1(name1, name2):
    '函数说明文档可在此处填写'
    print('函数创建测试')
    print('函数测试语句2')
    # print(name1 + name2 + 'test')
    return (name1 + name2)


print(function1.__doc__)
help(function1)
print(function1(5, 2))

# 关键字参数&默认参数


def SaySome(name='name', words='words'):
    print(name + '->' + words)


SaySome(words='第二个参数', name='第一个参数')
SaySome()

# 收集参数，以元组收集参数，若有其他参数，需要使用关键字参数货默认参数


def test(*param, exp):
    print('参数的长度是：', len(param))
    print('第二个参数是：', param[1])
    print(type(param))
    print(exp)


test(1, '字符串', 3.14, 5, 6, 7, exp=8)

# 局部变量&全局变量


def discounts(price, rate):
    final_price = price * rate
    old_price = 50
    print('函数内old_price的值是：', old_price)
    old_price
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣:'))
new_price = discounts(old_price, rate)
print('折扣价：', new_price)
print('修改后的old_price', old_price)
old_price

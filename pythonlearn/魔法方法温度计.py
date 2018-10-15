#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 22:10:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instacne, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


Temp = Temperature()
Temp.fah = 100
# 执行描述符类Fahrenheit(),在Fahrenheit()__set__中，设置了Temperature()类的cel,因此执行了描述符类Celsius(),完成了转换
Temp.cel = 18
print(Temp.fah)

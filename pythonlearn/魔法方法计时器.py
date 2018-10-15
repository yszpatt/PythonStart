#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-03 21:16:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import time as t


class MyTime():
    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
# 用于直接调用class时返回字符串

    def __str__(self):
        return self.prompt

    __repr__ = __str__
# 定义时间相加

    def __add__(self, other):
        self.prompt = "共运行了"
        self.result = []
        for index in range(6):
            self.result.append(self.lasted[index] + other.lasted[index])
            if self.result[index]:
                self.prompt += (str(self.result[index]) + self.unit[index])
        return self.prompt

    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()停止计时"
        print("计时开始")

    def stop(self):
        if not self.begin:
            print("请先用start()开始计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束")
    # 内部方法计算时间

    def _calc(self):
        self.lasted = []
        self.prompt = "共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
        if self.lasted[index]:
            self.prompt += str(self.lasted[index]) + self.unit[index]
        self.begin = 0
        self.end = 0

        # print(self.prompt)


t1 = MyTime()
t2 = MyTime()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

list_ = []
for i in range(1, 11):
    list_.append(int(input('输入一个数字:')))
print(list_)
list_.sort(reversed=True)
print(list_)

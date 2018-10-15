#!/usr/bin/env python
# # coding:utf-8
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。


score = int(input("输入学生成绩："))
g = (score >= 90 and score <= 100) and "A" or (
    (score >= 60 and score < 90) and "B" or ((score < 60 and score >= 0) and "C" or "error"))
print(g)

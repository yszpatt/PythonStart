#!/usr/bin/env python
# coding:utf-8
# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！

for n in range(0, 3):
    username = input("请输入用户名：")
    password = input("输入密码：")

    if username == "seven" and password == "123":
        print("登录成功！")
        quit()
    else:
        print("登录失败")

print("超过3次，登录失败")
quit()

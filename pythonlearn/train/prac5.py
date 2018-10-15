#!/usr/bin/env python
# coding:utf-8
# 输入三个整数x,y,z，请把这三个数由小到大输出。

# x = int(input("x:"))
# y = int(input("y:"))
# z = int(input("z:"))

x = 3
y = 5
z = 4
l = [x, y, z]
l.sort()
print(l)
l.reverse()
print(l)

a = {"x": x, "y": y, "z": z}
print(a)

for w in sorted(a, key=a.__getitem__):
    print(w, a[w])

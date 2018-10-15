#!/usr/bin/env python
# coding:utf-8
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x**3 + y**3 + z**3 == x * 100 + y * 10 + z:
                print(x * 100 + y * 10 + z)



print([i for i in range(100, 1000) if (i // 100)**3 +(i // 10%10)**3 + (i % 10)**3 == i])


for i in range(100, 1000):
    s = str(i)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == i:
        print(i)


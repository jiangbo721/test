# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: Josephus.py
# ide: PyCharm
# time: 2019-04-25 18:27

# 圆圈中最后剩下的数字(约瑟夫环问题)
# 题目：0, 1, … , n-1 这 n 个数字排成一个圈圈，从数字 0 开始每次从圆圏里删除第 m 个数字。
# 求出这个圈圈里剩下的最后一个数字。

def josephus(n, m):
    josephus_circle = [i for i in range(n)]
    while n > 1:
        if n >= m:
            del josephus_circle[m - 1]
            josephus_circle = josephus_circle[m - 1:] + josephus_circle[:m - 1]
            n -= 1
        else:
            while m > n:
                m -= n
            del josephus_circle[m - 1]
            josephus_circle = josephus_circle[m - 1:] + josephus_circle[:m - 1]
            n -= 1
    print josephus_circle

josephus(10, 3)
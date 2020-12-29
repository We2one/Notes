#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Fibonacci_sequence.py
@time: 2020/12/23 16:25
@IDE: PyCharm
@desc: 斐波那契数列

"""


# 两个变量存储
def fibo2(n):
	if n == 0 or n == 1:
		return n
	n1, n2 = 0, 1
	num = 0
	for i in range(2, n+1):
		num = n1 + n2
		n1 = n2
		n2 = num
	return num


print(fibo2(4))


# 列表保存
def fibo1(n):
	res = [0, 1, 1]
	while len(res) <= n:
		res.append(res[-1]+res[-2])
	return res[n]


# print(fibo1(8))


# 递归
def fibo(n):
	if n == 0 or n == 1:
		return n
	return fibo(n-1) + fibo(n-2)


# print(fibo(4))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 14:35
# @Author  : SCZ
# @File    : 循环.py

names = ['Michael', 'Bob', 'Tracy']
for x in names:
    print(x)
print('打印列表中的每个字段')
print('--'*10)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
print('1-10求和')
print('--'*10)

sum=0
for x in range(11):
    sum += x
print(sum)
print('1-10求和')
print('--'*10)

sum=0
n=99
while n>0:
    sum+=n
    n-=2
print(sum)
print('100以下奇数求和')
print('--'*10)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
print('--'*10)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
print('--'*10)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 14:10
# @Author  : SCZ
# @File    : 条件判断.py

age=18
if age>18:
    print('your age is %d'%age)
    print('you are adult')
elif age==18:
    print('your age is ',age)
    print('you will be adult!')
else:
    print('your age is', age)
    print('you are teenager')

print('--'*10)
if age:
    print('True')
print('只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。')
print('--'*10)



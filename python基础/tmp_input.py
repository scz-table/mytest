#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 21:01
# @Author  : SCZ
# @File    : tmp_input.py


#tmp_var=input('请输入：')
#print('您正在输入:“',tmp_var,'”')

birth=input('请输入您在哪一年出生:')
if birth.isdigit():
    birth=int(birth)
    if birth<2000:
        print('您在2000前出生！')
    elif birth==2000:
        print('您出生在2000年！')
    else:
        print('您在2000后出生！')
else:
    print('请输入数字！')
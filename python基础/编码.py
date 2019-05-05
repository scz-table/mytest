#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 21:22
# @Author  : SCZ
# @File    : 编码.py
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

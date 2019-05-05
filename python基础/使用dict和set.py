#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 14:46
# @Author  : SCZ
# @File    : 使用dict和set.py
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
c={'s':99,'t':89}
print(d['Michael'])
print(c['s'])
c['s']='替换元素'  #key存在时会替换key所对应的值
c['f']='替换元素'  #key不存在时会创建一个对应关系
print(c['s'])
print(c['f'])
#print(c['g'])  #找不到该元素就会报错
print('g' in c)  #通过in查找g是否在字典c中
print(c.get('g'))  #通过get查找g是否在字典c中,默认返回None，注意：返回None的时候Python的交互环境不显示结果。
print(c.get('g',-1))  #通过get查找g是否在字典c中,改变默认返回值
print(d.pop('Bob'))  #pop删除时返回关键字所对应的的值
print(d)
print(d.keys())
print(d.values())
print(d.items())
del d['Tracy']     #del 的方式删除不会有返回值
print(d)
print(c)
c.popitem()
print(c)
qq=c.copy( )
ww=c
c['s']='再次替换元素'
print('显示qq字典：',qq)
print('显示ww字典：',ww)
print('显示c字典：',c)
c=1000
print('显示c变量：',c)

print('''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合.''')

list1=[1,2,3,3,5,7,1,4,4,5,6]
set1=set(list1)

print('作为输入的list显示结果为：',list1)
print('创建了一个set的显示结果为：',set1)
set1.add(99)
print('集合通过add函数增加了一个元素为：',set1)
set1.remove(6)
print('集合通过remove函数删除了一个元素为：',set1)




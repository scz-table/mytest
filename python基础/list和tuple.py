#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 20:52
# @Author  : SCZ
# @File    : list和tuple.py

classmate=['Michel','Bob','Tracy']
print('打印列表的全部值：',classmate)
print('打印列表的长度：',len(classmate))
print('--'*10)

print('尝试用角标打印列表的值：')
print(classmate[0])
print(classmate[1])
print(classmate[2])
#print(classmate[3])
print('打印列表的最后一个值:',classmate[len(classmate)-1])
print('--'*10)

print('尝试用循环打印列表的值：')
for i in classmate:
    print(i)
print('--'*10)

print('列表查找的5种方法：')
print('Michel' in classmate)
print('Michel' not in classmate)
print(classmate.count('Michel'))
print(classmate.index('Michel'))
#print(classmate.index('Michel111'))
print(classmate.index('Michel',0,1))
#print(classmate.find('Michel'))
print('--'*10)

print('尝试用循环打印列表的序号和值：')
for i,k in enumerate(classmate):
    print(i+1,'--',k)
print('--'*10)

print('向列表追加值append函数：')
classmate.append('adma')
print(classmate)
print('--'*10)

print('向列表追加值insert函数：')
classmate.insert(1,'Jack')
print(classmate)
print('--'*10)

print('删除列表最后的值pop函数：')
classmate.pop()
print(classmate)
print('--'*10)

print('删除列表指定的值pop函数：')
classmate.pop(1)
print(classmate)
print('--'*10)

print('删除列表指定的值del函数：')
del classmate[1]
print(classmate)
print('--'*10)

print('替换列表指定的值：')
classmate[0]='Sarah'
print(classmate)
print('--'*10)

print('替换列表指定的值：')
classmate[0]='Sarah'
print(classmate)
print('--'*10)

print('列表包含列表：')
classmate.append(['Sarah','anddd'])
print(classmate)
print('--'*10)

print('列表包含元组：')
classmate.append(('Sarah','anddd'))
print(classmate)
print('--'*10)

print('列表包含集合：')
classmate.append({'Sarah','anddd'})
print(classmate)
print('--'*10)

'''
print('列表包含字典：')
classmate.append({'Sarah'：'anddd'})
print(classmate)
print('--'*10)
'''

print('元组至少包含一个逗号：')
classmate_tuble=(2,)
print((2))
print(classmate_tuble)
print('--'*10)

print('元组至少包可变的元素时，该元素也可变：')
t = ('a', 'b', ['A', 'B'])
print(t )
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

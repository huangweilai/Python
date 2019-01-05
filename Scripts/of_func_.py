#!/usr/bin/env python
# @author=huangwl

import random
"""
# 内置函数
a = [1,2,3,4,]
b = [1,2,3,4,None]
all(a)
print(bool(all(a)))
print(bool(all(b)))
print(bool([]))         #False
print(bool(""))         #False
print(bool({}))         #False

print(bool(any(["",[],{},None,1])))     #any有一个为真，则为真
print(bool(all(["",[],{},None,1])))     #all有一个为假，则为假

print(bin(10))          #二进制
p = bytearray("黄",encoding='utf-8')
print(p)

f = lambda x: x+1
f(5)
print(f(5))
print(callable(f))
print(ord('a'))
print(chr(99))

print(random.randint(1,1000))

print(dir())

mobile = ["apple","huawei","xiaomi"]
for i,item in enumerate(mobile,1):
    print(i,item)
"""
# map
n1 = [11,22,33,44,]
new_n1 = map(lambda x: x+100,n1)
ret_new_n1 = list(new_n1)
print(ret_new_n1,'\n')

# 2
def func_(x):
    return x+100

new_n2 = map(func_,n1)
print(list(new_n2),'\n')

# filter
def fun_(i):
    if i>33:
        return True
    else:
        return False

ret_filter = filter(fun_,n1)
print(list(ret_filter),'\n')

print(globals())        #全局变量
print(locals())         #局部变量
print(oct(10))






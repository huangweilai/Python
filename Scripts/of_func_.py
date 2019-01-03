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
"""
mobile = ["apple","huawei","xiaomi"]
for i,item in enumerate(mobile,1):
    print(i,item)



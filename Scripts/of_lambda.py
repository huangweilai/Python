#!/usr/bin/env python
# @author=huangwl

def func(a):
    b = a + 1
    return a
res = func(4)
print(res)

# lambda表达式,简单函数的表达方式
func = lambda a: a+1
r = func(99)
print(r)

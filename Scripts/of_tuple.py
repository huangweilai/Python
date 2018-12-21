#!/usr/bin/env python
# @author=huangwl

#多种方式定义元祖
"""
tu = (11,22,33,)
tu = tuple((11,22,33,))
tu = tuple([11,22,33,])
"""
#列表转换元祖
"""
li = [11,22,33,]
tu = tuple(li)
l = list(tu)
"""

t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t,'\n')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


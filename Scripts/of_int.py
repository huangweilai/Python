#!/usr/bin/env python
# @author=huangwl

a = [11,22,33]
print(a)
print(type(a))


a = int(13)
print(a.bit_length())

b = int(-19)
print(abs(b))
print(b.__abs__())      #绝对值
print(b.__add__(100))
ret = b + 100
print(ret)

all_item = 95
page = 10
res = all_item.__divmod__(10)   #求商，取余数
print(res)

print(a.__eq__(b))      #判断是否相等

print(type(a))
res1 = a.__float__()    #浮点型
print(type(res1))

c = int(25)
res2 = c.__floordiv__(a)    #地板除
print(res2)
res3 = c.__divmod__(5)      #c/5  商，余数
print(res3)
res4 = c.__rdivmod__(5)     #5/c  余数<商
print(res4)

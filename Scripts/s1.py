#!/usr/bin/env python
# @author=huangwl

# a = [11,22,33]
# print(a)
# print(type(a))


a = int(13)
print(a.bit_length())

b = int(-19)
print(b.__abs__())      #绝对值
print(b.__add__(100))

all_item = 95
page = 10
res = all_item.__divmod__(10)   #求商，取余数
print(res)




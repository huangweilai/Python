#!/usr/bin/env python
# @author=huangwl

"""
将以下集合中大于66的值保存至字典的第一个key中，小于或等于66的保持至第二个key中。
[11,22,33,44,55,66,77,88,99]
{'k1': >66,'k2': <=66}
dic = {}
"""

"""part1


L1 = []     #大于66
L2 = []     #小于66
dic = {}
all_list = [11,22,33,44,55,66,77,88,99]

for i in all_list:
    if i > 66:
        L1.append(i)
    else:
        L2.append(i)

dic['k1'] = L1
dic['k2'] = L2

print(dic['k1'])
print(dic['k2'])

"""

"""part2
dic = {}
all_list = [11,22,33,44,55,66,77,88,99]

for i in all_list:
    if i>66:
        if 'k1' in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i,]
    else:
        if 'k2' in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i,]

print(dic['k1'])
print(dic['k2'])

"""

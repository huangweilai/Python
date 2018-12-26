#!/usr/bin/env python
# @author=huangwl

import copy
"""
copy.copy()         #浅拷贝
copy.deepcopy()     #深拷贝
"""

"""
#赋值
a1 = 123
b1 = 123
c1 = a1
print(id(a1))
print(id(b1))
print(id(c1))


a2 = copy.copy(a1)          #浅拷贝
print(id(a1))
print(id(a2),'\n')

a3 = copy.deepcopy(a1)      #深拷贝
print(id(a1))
print(id(a3),'\n')
"""

#其他，元祖，列表，字典
"""
n1 = {"k1":"huang","k2":'123',"k3":['weilai',22,]}
n2 = n1
n3 = copy.copy(n1)
n4 = copy.deepcopy(n1)
print('n1:',id(n1))
print('n2:',id(n2))
print('n3:',id(n3))
print('n4:',id(n4),'\n')

print('n1[k3]:',id(n1['k3']))
print('n3[k3]:',id(n3['k3']),'\n')

print('n1[k3]:',id(n1['k3']))
print('n4[k3]:',id(n4['k3']),'\n')

"""


















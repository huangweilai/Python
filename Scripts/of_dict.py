#!/usr/bin/env python
# @author=huangwl

"""
dic = {'k1':'v1','k2':'v2'}

# dic = dict(k1='v1',k2='v2')
# new_dic = dic.fromkeys(['k1','k2','k3'],'v1')         #获取key，形成新的字典
# print(new_dic)


print(dic['k1'])
print(dic['k2'])
print(dic['k3'])
print(dic.get('k1'))
print(dic.get('k2'))
print(dic.get('k3','huangwl'))              #k3不存在时，'k3'='huangwl'


print(dic)
print(dic.keys())               #获取key
print(dic.values())             #获取values
print(dic.items(),'\n')              #获取键值对

#循环

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

for k,v in dic.items():
    print(k,v)
    

dic.pop('k2')       #必须指定一个key
dic.popitem()       #随机删除一组
dic['k3'] = 123
dic.setdefault('k4')        #设置默认值
dic.update({'k3':123})      #更新字典
print(dic)
"""








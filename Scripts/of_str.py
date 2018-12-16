#!/usr/bin/env python
# @author=huangwl


name = 'HUANGWL'
name = str('HUANGWL')
print(type(name))
print(dir(name))
print(name.__contains__('h'))       #包含
print(name.capitalize())            #首字母大写
print(name.casefold())              #大写转小写
print(name.center(20))              #居中
print(name.center(20,'*'))          #居中，填充*

a = 'awawaw'
print(a.count('w'))                 #统计
print(a.count('w',0,10))            #统计,设定起始位置和结束位置
print(a.encode('gbk'))              #utf-8转gbk编码
print(a.endswith('w'))              #判断字符是否为结尾
print(a.endswith('w',0,3))          #判断字符是否为结尾

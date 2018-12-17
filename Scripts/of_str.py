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
print(name.center(20,'*'),'\n')     #居中，填充*

a = 'awawaw'
print(a.count('w'))                 #统计
print(a.count('w',0,10))            #统计,设定起始位置和结束位置
print(a.encode('gbk'))              #utf-8转gbk编码
print(a.endswith('w'))              #判断字符是否为结尾
print(a.endswith('w',0,3),'\n')     #判断字符是否为结尾

#tab转换位空格
My_Name = 'h\tuang'
res = My_Name.expandtabs()
print(len(res))
print(res,'\n')

#查找字符串
b = 'test'
res_b = b.find('x')
res_b_index = b.index('t')
print(res_b)
print(res_b_index)


c = "test  {0}"
res_c = c.format('again')
print(res_c)

d = "huawei {phone1} and {phone2}"
res_d = d.format(phone1 = 'xiaomi',phone2 = 'apple')
print(res_d)
#字符串拼接
li = ['o','n','e','p','l','u','s']
res_li = "".join(li)
res_li1 = "-".join(li)
res_li2 = "_".join(li)
print(res_li)
print(res_li1)
print(res_li2)

f = 'qwertyyyyyyyyyyy'
res_f = f.partition('er')           #分割
res_f1 = f.replace('y','o')         #替换
res_f2 = f.replace('y','o',1)         #替换
print(res_f)
print(res_f1)
print(res_f2)

g = """
aa
bb
cc"""
res_g = g.splitlines()
# res_g1 = g.splitl('\n')
print(res_g)
# print(res_g1)


